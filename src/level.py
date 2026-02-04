from Platform import Platform
import pygame



test_level: pygame.sprite.Group = pygame.sprite.Group()
test_level.add(
    Platform((  0, 500), None, width=1000, height=  50, state='s'),
    Platform((200, 400), None, width= 200, height=  30, state='s'),
    Platform((100, 450), None, width= 200, height=  30, state='p'),
    Platform((500, 300), None, width= 150, height=  30, state='p')
)

#collisions = pygame.sprite.spritecollide(Player, rendered_platforms, False)
