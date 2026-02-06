import pygame
import os
from Constants import terminal_velocity, friction, gravity, walk_frame, base_path


class Character(pygame.sprite.Sprite):
    global walk_frame
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
        self.cur_act = self.move_left
        self.act_strt_time = tt
    def move_right(self, tt) -> None:
        self.acceleration.x = self.walkspeed
        self.look_right()
        self.cur_act = self.move_right
        self.act_strt_time = tt
    
    def move_jump (self, tt) -> None:
        self.acceleration.y -= 2
        self.isGrounded = False
        facingMult = {"r": 1, "l": -1}
        self.acceleration.x += 5 * facingMult[self.facing]
        self.cur_act = self.move_jump
        self.act_strt_time = tt


    def move_climb (self, collisionslist, tt) -> None:
        
        for thing in collisionslist:
            if thing.state != 's': # solid
                return
            
            if abs(self.rect.left - thing.rect.right) < 10 or abs(self.rect.right - thing.rect.left) < 10:
                if (self.velocity.y > -2.5):
                    self.velocity.y = -6
                    self.cur_act = self.move_climb
                    self.act_strt_time = tt
        return
    
    def look_left(self) -> None:
        if self.facing == "l":
            return
        self.facing = "l"
        self.image = self.base_image
    def look_right(self) -> None:
        if self.facing == "r":
            return
        self.facing = "r"
        self.image = pygame.transform.flip(self.base_image, True, False)
    
    def nothing(self, tt) -> None:
        self.cur_act = self.nothing
        self.act_strt_time = tt
        return

    def update(self,dt):
        
        if (self.acceleration.y < gravity and not self.isGrounded):
            self.acceleration.y += 0.1
        
        self.velocity += self.acceleration * (dt+1)

        self.velocity.y = min(self.velocity.y, terminal_velocity)
        self.velocity.x = max(-self.maxspeed, min(self.velocity.x, self.maxspeed))
        
        if self.acceleration.x == 0:
            self.velocity.x *= friction #decellerate if not moving (acceleration = 0)
        
        if (self.cur_act == self.move_left) or (self.cur_act == self.move_right):
            current_image = os.path.join(base_path,
                                    "assets",
                                    "PlayerAnim",
                                    "Run",
                                    f"{int(self.act_strt_time % 4) + 1}.png"
                                    )
            #print(int(self.act_strt_time*60/4)+1)
            self.image = pygame.image.load(current_image).convert_alpha()
            self.image = pygame.transform.scale(self.image, (80,120))
            
            
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

    def select_action(self,):
        
        pass

    def update(self, dt) -> None:
        super().update(dt)
        if self.cur_act is self.nothing:
            self.cur_act = self.move_left
            self.act_strt_time = dt
        #finish later
        
        
