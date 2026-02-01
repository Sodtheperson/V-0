# Example file showing a circle moving on screen
import pygame
import pygame.math as pgm
from CharacterClass import Character
from Constants import *

# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

font = pygame.font.SysFont(None, 30)


Player = Character(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 300, pgm.Vector2(0,0), pgm.Vector2(0,0), 5)


while running:
    pygame.display.set_caption("SOMEBODY HELP ME") #little bar at the top
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    Player.rect.center = Player.pos

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    text_surface = font.render(f"Acceleration: {Player.acceleration} | Velocity: {Player.velocity}", True, (255, 255, 255)) #text on screen
    text_rect = text_surface.get_rect() #size of text
    text_rect.center = (400, 150) #position of text
    screen.blit(text_surface, text_rect) #push text to screen
    screen.blit(Player.image, Player.rect)
    
    
    pygame.draw.circle(screen, "blue", Player.rect.center, 20)

    keys = pygame.key.get_pressed()
    mod_keys = pygame.key.get_mods()

    if keys[pygame.K_w]:
        print("there arent any walls to climb yet idiot")
    if keys[pygame.K_s]:
        print("hi")
        #either crouching or something else idk
        
    """SAHIL PLEASE HELP ME I DONT KNOW HOW TO ADD JUMPING"""
    
    if keys[pygame.K_a]:
        Player.acceleration.x = -0.2
    elif keys[pygame.K_d]:
        Player.acceleration.x = 0.2 
    else:
        Player.acceleration.x = 0
        
    #Accelerate if moving left/right
    
    Player.velocity += Player.acceleration
    
    #add velocity to acceleration
    
    if Player.acceleration.x == 0:
        Player.velocity.x *= friction #decellerate if not moving (acceleration = 0)
    if 0.1 >= Player.velocity.x and Player.velocity.x >= -0.1 and Player.acceleration.x == 0:
        Player.velocity.x = 0 #set to 0 at small numbers to eliminate scientific configuration Ex. 1.273 * e^10
        
    if abs(Player.velocity.x) > Player.maxspeed: #limit to maxspeed
        if Player.velocity.x > 0:
            Player.velocity.x = Player.maxspeed 
        else:
            Player.velocity.x = -Player.maxspeed
        
    Player.pos += Player.velocity
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

