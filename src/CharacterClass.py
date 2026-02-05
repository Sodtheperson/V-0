import pygame
import os
from Constants import terminal_velocity, friction, gravity

class Character(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2, walkspeed: float, maxspeed: int) -> None:
        
        super().__init__()
        
        base_path = os.path.dirname(__file__)
        asset_path = os.path.join(base_path,"..","assets","hahahah.png")
        
        self.image = pygame.image.load(asset_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (40,80))
        self.base_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.facing = "r" # l is left, r is right

        # -- MAIN INFORMATION 👍👍👍👍👍👍😁
        
        self.pos: pygame.Vector2 = pos
        self.walkspeed: float = walkspeed
        self.acceleration: pygame.Vector2 = pygame.Vector2(0,0)
        self.velocity: pygame.Vector2 = pygame.Vector2(0,0)
        self.maxspeed: int = maxspeed
        self.isGrounded: bool = True
    #
    
    def move_left (self) -> None:
        self.acceleration.x = -self.walkspeed
        self.look_left()
    def move_right(self) -> None:
        self.acceleration.x = self.walkspeed
        self.look_right()
    
    def move_jump (self) -> None:
        self.acceleration.y -= 2
        self.isGrounded = False
        facingMult = {"r": 1, "l": -1}
        self.acceleration.x += 5 * facingMult[self.facing]
    def move_climb (self, collisionslist) -> None:
        for thing in collisionslist:
            print("Called")
            if thing.state != 's': # solid
                return
            
            if min(abs(self.rect.bottom - thing.rect.top),abs(self.rect.top - thing.rect.bottom)) > min(abs(self.rect.left - thing.rect.right),abs(self.rect.right - thing.rect.left)):
                if (abs(self.rect.bottom - thing.rect.top) <= 100) and (self.velocity.y > -2.5):
                    self.velocity.y -= 4
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

    def update(self,dt):
        
        if (self.acceleration.y < gravity and not self.isGrounded):
            self.acceleration.y += 0.1
        
        self.velocity += self.acceleration * (dt+1)

        self.velocity.y = min(self.velocity.y, terminal_velocity)
        self.velocity.x = max(-self.maxspeed, min(self.velocity.x, self.maxspeed))
        
        if self.acceleration.x == 0:
            self.velocity.x *= friction #decellerate if not moving (acceleration = 0)
        if 0.5 >= self.velocity.x and self.velocity.x >= -0.5 and self.acceleration.x == 0:
            self.velocity.x = 0 #set to 0 at small numbers to eliminate scientific configuration Ex. 1.273 * e^10

        self.pos += self.velocity
        self.rect.center = (int(self.pos.x), int(self.pos.y)) # safer conversion
    #

    def __str__(self):
        return "Character at " + str(self.pos)
#

class Dog(Character):
    def __init__(self, pos: pygame.Vector2, walkspeed: float, maxspeed: int) -> None:
        
        super().__init__(pos, walkspeed, maxspeed)
        
        base_path = os.path.dirname(__file__)
        asset_path = os.path.join(base_path,"..","assets","hahahah.png")
        
        self.image = pygame.image.load(asset_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (80,30))
        self.base_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.facing = "r" # l is left, r is right
        
        self.cur_act = self.nothing
        self.act_strt_time = 0
    #

    def nothing(self):
        pass

    def update(self, dt) -> None:
        super().update(dt)
        if self.cur_act is self.nothing:
            self.cur_act = self.move_left
            self.act_strt_time = dt
        #finish later
        
        