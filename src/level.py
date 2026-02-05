from Platform import Platform
import pygame



test_level: pygame.sprite.Group = pygame.sprite.Group()
test_level.add(
    Platform((  0, 500), ( 50, 50, 50), width=1000, height=  50, state='s'),
    Platform((200, 350), (100, 50, 30), width= 200, height=  30, state='s'),
    Platform((300, 300), (200, 50, 30), width= 200, height=  30, state='u'),
    Platform((100, 450), (  0, 82, 85), width= 200, height=  30, state='p'),
    Platform((500, 400), ( 52,200, 48), width= 150, height=  30, state='s')
)

#collisions = pygame.sprite.spritecollide(Player, rendered_platforms, False)
