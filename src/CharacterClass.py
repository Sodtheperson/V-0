import pygame
import os

class Character(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2, walkspeed: int, acceleration: pygame.math.Vector2, velocity: pygame.math.Vector2, maxspeed: int) -> None:
        
        super().__init__()
        
        base_path = os.path.dirname(__file__)
        asset_path = os.path.join(base_path,"..","assets","hahahah.png")
        
        self.image = pygame.image.load(asset_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (64,64))
        self.base_image = self.image
        self.rect = self.image.get_rect(center=pos)
        self.facing = "r" # l is left, r is right

        # -- MAIN INFORMATION 👍👍👍👍👍👍😁
        
        self.pos: pygame.Vector2 = pos
        self.walkspeed: int = walkspeed
        self.acceleration: pygame.Vector2 = pygame.Vector2(0,0)
        self.velocity: pygame.Vector2 = pygame.Vector2(0,0)
        self.maxspeed: int = maxspeed
        self.isGrounded: bool = True
    #
    
    def move_left (self) -> None:
        self.acceleration.x = -self.walkspeed
        self.look_left()
    def move_right(self) -> None:
        self.acceleration.x =  self.walkspeed
        self.look_right()
    
    def move_jump (self, strength: int = 1) -> None:
        self.acceleration.y -= 2
        self.isGrounded = False
        facingMult = {"r": 1, "l": -1}
        self.acceleration.x += 5 * facingMult[self.facing] * strength
    
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

    

    def __str__(self):
        return "Character at " + str(self.pos)