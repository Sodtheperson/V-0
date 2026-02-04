from Platform import Platform
import pygame



test_level: pygame.sprite.Group = pygame.sprite.Group()
test_level.add(
    Platform(pos=(   0, 500), width=1000, height=  50, image=(50,50,50), state='s')
#    Platform(pos=(200, 400), width= 200, height=  30, image="ground.png", state='s'),
#    Platform(pos=(100, 450), width= 200, height=  30, image="ground.png", state='p'),
#    Platform(pos=(500, 300), width= 150, height=  30, image="ground.png", state='p')
)

#collisions = pygame.sprite.spritecollide(Player, rendered_platforms, False)
