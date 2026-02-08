import os
import pygame

screen_size: tuple = (1200, 700)

friction = 0.85
air_resistence = 0.8
terminal_velocity = 10
gravity = 0.7

pygame.mixer.init()

base_path = os.path.dirname(os.path.dirname(__file__))  # go up from src
asset_path = os.path.join(base_path,"assets")