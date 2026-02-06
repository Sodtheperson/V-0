from Platform import Platform
import pygame
import Constants 

class CurrentLevel:
    num = 0
    
total_levels : list = []

test_level: pygame.sprite.Group = pygame.sprite.Group()
test_level.add(
    Platform((  0, 500), ( 50, 50, 50), width=1000, height=  50, state='s'),
    Platform((200, 350), (100, 50, 30), width= 200, height=  30, state='s'),
    Platform((300, 300), (200, 50, 30), width= 200, height=  30, state='u'),
    Platform((100, 450), (  0, 82, 85), width= 200, height=  30, state='p'),
    Platform((500, 400), ( 52,200, 48), width= 150, height=  30, state='s'),
    Platform((  100, Constants.screen_size[1] - 450), (255,255,255), width=50, height=100, state='u'), # Door ?
)
total_levels.append(test_level)

box_level: pygame.sprite.Group = pygame.sprite.Group()
box_level.add(
    Platform((  0, Constants.screen_size[1] - 50), ( 50, 50, 50), width=Constants.screen_size[0], height=  50, state='s'), # floor
    Platform((  0, 0), ( 50, 50, 50), width=Constants.screen_size[0], height=  50, state='s'), # Ceiling
    Platform((  0, 0), ( 50, 50, 50), width=50, height=Constants.screen_size[1], state='s'), # Left Wall
    Platform((  Constants.screen_size[0] - 50, 0), ( 50, 50, 50), width=50, height=Constants.screen_size[1], state='s'), # Right
    Platform((  Constants.screen_size[0]-100, Constants.screen_size[1] - 150), (255,255,255), width=50, height=100, state='u'), # Door ?
)
total_levels.append(box_level)
#collisions = pygame.sprite.spritecollide(Player, rendered_platforms, False)
