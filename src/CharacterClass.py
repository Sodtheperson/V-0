import pygame
import os
from Constants import terminal_velocity, friction, gravity, base_path


class Character(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2, walkspeed: float, maxspeed: int, animation_folder: str) -> None:
        
        super().__init__()
        
        self.base_path = os.path.dirname(os.path.dirname(__file__))
        self.asset_path = os.path.join(self.base_path,"assets", animation_folder)
        
        self.image = pygame.image.load(os.path.join(self.asset_path, "hahahah.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,80))
        self.base_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.facing = "r" # l is left, r is right

        self.cur_act = self.nothing
        self.act_strt_time = 0

        # -- MAIN INFORMATION 👍👍👍👍👍👍😁
        
        self.pos: pygame.Vector2 = pos
        self.walkspeed: float = walkspeed
        self.acceleration: pygame.Vector2 = pygame.Vector2(0,0)
        self.velocity: pygame.Vector2 = pygame.Vector2(0,0)
        self.maxspeed: int = maxspeed
        self.isGrounded: bool = True
        
    #
    
    def move_left (self, tt) -> None:
        self.acceleration.x = -self.walkspeed
        self.look_left()
        if self.cur_act != self.move_left:
            self.cur_act = self.move_left
            self.act_strt_time = tt
    def move_right(self, tt) -> None:
        self.acceleration.x = self.walkspeed
        self.look_right()
        if self.cur_act != self.move_right:
            self.cur_act = self.move_right
            self.act_strt_time = tt
    
    def move_jump (self, tt) -> None:
        self.acceleration.y -= 2
        self.isGrounded = False
        facingMult = {"r": 1, "l": -1}
        self.acceleration.x += 5 * facingMult[self.facing]
        if self.cur_act != self.move_jump:
            self.cur_act = self.move_jump
            self.act_strt_time = tt


    def move_climb (self, collisionslist, tt) -> None:
        self.acceleration.y -= 0.001
        for thing in collisionslist:
            if thing.state != 's': # solid
                return
            
            if abs(self.rect.left - thing.rect.right) < 10 or abs(self.rect.right - thing.rect.left) < 10:
                if (self.velocity.y > -2.5):
                    self.velocity.y = -6
                    if self.cur_act != self.move_climb:
                        self.cur_act = self.move_climb
                        self.act_strt_time = tt
        return
    
    def look_left(self) -> None:
        if self.facing == "l":
            return
        self.facing = "l"
    def look_right(self) -> None:
        if self.facing == "r":
            return
        self.facing = "r"
    
    def nothing(self, tt) -> None:
        if self.cur_act != self.nothing:
            self.cur_act = self.nothing
            self.act_strt_time = tt
        return

    def update(self, dt, tt):
        
        if (self.acceleration.y < gravity and not self.isGrounded):
            self.acceleration.y += 0.1
        
        self.velocity += self.acceleration * (dt+1)

        self.velocity.y = min(self.velocity.y, terminal_velocity)
        self.velocity.x = max(-self.maxspeed, min(self.velocity.x, self.maxspeed))
        
        if self.acceleration.x == 0:
            self.velocity.x *= friction #decellerate if not moving (acceleration = 0)
        
        if (self.cur_act == self.move_left) or (self.cur_act == self.move_right):
            current_image = os.path.join(self.asset_path,
                                    "Run",
                                    f"{(int((self.act_strt_time - tt)/8) % 4) + 1}.png"
                                    )


            raw_img = pygame.image.load(current_image).convert_alpha()
            tight_rect = raw_img.get_bounding_rect()

            cropped_img = raw_img.subsurface(tight_rect)

            if self.facing == 'l':
                self.base_image = pygame.transform.scale(cropped_img, (60,80))
            elif self.facing == 'r':
                self.base_image = pygame.transform.flip(pygame.transform.scale(cropped_img, (60,80)), True, False)
            
            self.image = self.base_image
        else:
            current_image = os.path.join(self.asset_path,
                                    "still.png",
                                    )
            raw_img = pygame.image.load(current_image).convert_alpha()
            tight_rect = raw_img.get_bounding_rect()

            cropped_img = raw_img.subsurface(tight_rect)
  
            self.image = pygame.transform.scale(cropped_img, (60,80))

        
        
        if 0.5 >= self.velocity.x and self.velocity.x >= -0.5 and self.acceleration.x == 0:
            self.velocity.x = 0 #set to 0 at small numbers to eliminate scientific configuration Ex. 1.273 * e^10

        self.pos += self.velocity
        self.rect.center = (int(self.pos.x), int(self.pos.y)) # safer conversion
        return

    def __str__(self):
        return "Character at " + str(self.pos)
#

class Animal(Character):
    def __init__(self, pos: pygame.Vector2, walkspeed: float, maxspeed: int, animation_folder: str) -> None:
        super().__init__(pos, walkspeed, maxspeed, animation_folder)
    #
    
    def move_jump_charge(self, tt) -> None:
        if self.cur_act != self.move_jump_charge:
            self.cur_act = self.move_jump_charge
            self.act_strt_time = tt
        return

    def move_sit(self, tt) -> None:
        if self.cur_act != self.move_sit:
            self.cur_act = self.move_sit
            self.act_strt_time = tt
        return
    

    def can_move_left(self, lvl) -> bool:
        
        self.rect.move_ip(self.walkspeed, 0)
        res = pygame.sprite.spritecollide(self, lvl, False)
        if res: # if Animal would hit wall by moving left
            self.rect.move_ip(-self.walkspeed, 0)
            return False
        
        self.rect.move_ip(0, 0.2)
        res = pygame.sprite.spritecollide(self, lvl, False)
        self.rect.move_ip(-self.walkspeed, -0.2)
        if res: # if Animal would be on floor by moving left (in floor by moving down + left)
            return False
        
        return True

    def can_move_right(self, lvl) -> bool:
        
        self.rect.move_ip(-self.walkspeed, 0)
        res = pygame.sprite.spritecollide(self, lvl, False)
        if res: # if Animal would hit wall by moving left
            self.rect.move_ip(self.walkspeed, 0)
            return False
        
        self.rect.move_ip(0, 0.2)
        res = pygame.sprite.spritecollide(self, lvl, False)
        self.rect.move_ip(self.walkspeed, -0.2)
        if res: # if Animal would be on floor by moving left (in floor by moving down + left)
            return False
        
        return True

    def select_action(self, tt, lvl):
        if not self.isGrounded:
            return
        
        can_left  = self.can_move_left (lvl)
        can_right = self.can_move_right(lvl)

        if can_left and can_right and self.cur_act == self.move_sit:
            if self.act_strt_time >= 3*60:
                self.cur_act = self.nothing
                self.act_strt_time = tt
            return
        elif self.cur_act == self.move_jump_charge:
            if self.act_strt_time >= 2*60:
                self.cur_act = self.nothing
                self.act_strt_time = tt
            return
        elif can_left:
            if self.cur_act != self.move_left:
                self.cur_act = self.move_left
                self.act_strt_time = tt
            return
        elif can_right:
            if self.cur_act != self.move_right:
                self.cur_act = self.move_right
                self.act_strt_time = tt
            return
        elif self.cur_act == self.move_sit and self.act_strt_time >= 10*60:
            if self.cur_act != self.move_jump:
                self.cur_act = self.move_jump
                self.act_strt_time = tt
            return
    #

    def update(self, dt, tt, lvl) -> None:
        super().update(dt, tt)
        self.select_action(tt, lvl)
        print(self.cur_act)
        self.cur_act(tt)
        #finish later
        
        
