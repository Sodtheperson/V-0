import pygame
import os
# I need to put a changable floor constant, so here it is
FloorLim = int


class Character(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2, walkspeed: int, acceleration: pygame.math.Vector2, velocity: pygame.math.Vector2, maxspeed: int) -> None:
        
        super().__init__()
        
        base_path = os.path.dirname(__file__)
        asset_path = os.path.join(base_path,"..","assets","hahahah.png")
        
        self.image = pygame.image.load(asset_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        
        # -- MAIN INFORMATION
        
        self.pos: pygame.Vector2 = pos
        self.walkspeed: int = walkspeed
        self.acceleration: pygame.Vector2 = pygame.Vector2(0,0)
        self.velocity: pygame.Vector2 = pygame.Vector2(0,0)
        self.maxspeed: int = maxspeed
        self.isGrounded: bool = True
    #

    def move_left
    
    def __str__(self):
        return str(self.pos)