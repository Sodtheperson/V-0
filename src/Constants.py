import pygame

friction = 0.85
air_resistence = 0.8
terminal_velocity = 10
gravity = 0.85


floors = [
    pygame.Rect(0, 500, 1000, 50),    # ground
    pygame.Rect(200, 400, 200, 30),  # platform
    pygame.Rect(100, 450, 200, 30),  # ladder platform
    pygame.Rect(500, 300, 150, 30),  # higher platform
]
