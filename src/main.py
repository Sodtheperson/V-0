# Example file showing a circle moving on screen
import pygame
import pygame.math as pgm
from CharacterClass import Character, Animal
from Constants import *
from level import *
from typing import Any
tt = 0
DEV_MODE = True #hi

#Helper function for collision. 

def collisions(Colidee : Character, Collidergroup : pygame.sprite.Group, RemoveColliderfromList : bool = False, E_key : bool = False) -> None:
    Colidee.isGrounded = False
    collisionslist = pygame.sprite.spritecollide(Colidee, Collidergroup, False)
    
    for obj in Collidergroup:
        if isinstance(obj, Button):
            obj.pressed = False
            obj.update()
    
    for thing in collisionslist:
        if thing.state != 'u': # uncollidable
            
            if thing.state == 's': # solid
                if min(abs(Colidee.rect.bottom - thing.rect.top),abs(Colidee.rect.top - thing.rect.bottom)) <= min(abs(Colidee.rect.left - thing.rect.right),abs(Colidee.rect.right - thing.rect.left)):
                    if abs(Colidee.rect.bottom - thing.rect.top) <= abs(Colidee.rect.top - thing.rect.bottom):
                        Colidee.rect.bottom = thing.rect.top
                        Colidee.velocity.y = 0
                        Colidee.isGrounded = True
                    else:
                        Colidee.rect.top = thing.rect.bottom
                        Colidee.velocity.y = 0
                else:
                    if abs(Colidee.rect.left - thing.rect.right) <= abs(Colidee.rect.right - thing.rect.left):
                        Colidee.rect.left = thing.rect.right
                        Colidee.velocity.x = 0
                        Colidee.acceleration.x = 0
                    else:
                        Colidee.rect.right = thing.rect.left
                        Colidee.velocity.x = 0
                        Colidee.acceleration.x = 0
                                
                #VERY IMPORTANT: Updating the datatype Character 's rect must be done while updating it's pos or else MAJOR consequences
                Colidee.pos = pygame.math.Vector2(Colidee.rect.center)
            
            elif (Colidee.rect.bottom - Colidee.velocity.y) <= thing.rect.top: #if partially solid and was above previosely
                Colidee.rect.bottom = thing.rect.top
                Colidee.velocity.y = 0
                Colidee.isGrounded = True
                Colidee.pos = pygame.math.Vector2(Colidee.rect.center)
        else: # Object Detection
            if isinstance(thing, Button):
                thing.pressed = True
                thing.update()
                    

            if thing.isDoor == True and E_key: # Door detection
                Level.num += 1
                Player.pos = Level.spawn_pos[Level.num]
                Player.rect.center = Level.spawn_pos[Level.num]
    return
#

# Finds and Returns the longest group passed
def maxGroup(group: list[Any], other: list[Any]):
    if len(group) >= len(other):
        return group
    else:
        return other
#

# pygame setup
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
clock = pygame.time.Clock()
running = True
dt = 0

font = pygame.font.SysFont(None, 30)

Player = Character(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 0.2, 5, "PlayerAnim")
Dog = Animal(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 0.3, 6, "PlayerAnim")

SURPRISE = pygame.mixer.Sound(os.path.join(asset_path, "hi.wav"))

Player.acceleration.y = 1
while running:
    

    pygame.display.set_caption("SOMEBODY HELP ME") #little bar at the top
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    
    text_surface = font.render(f"Acceleration: {Dog.acceleration} | Velocity: {Dog.velocity} | Grounded: {Dog.isGrounded}", True, (255, 255, 255)) #text on screen
    text_rect = text_surface.get_rect() #size of text
    text_rect.center = (400, 150) #position of text
    screen.blit(text_surface, text_rect) #push text to screen
    

    keys = pygame.key.get_pressed()
    mod_keys = pygame.key.get_mods()

    
    #reset animations
    if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_e]:
        Player.nothing(tt)


    if keys[pygame.K_w] and Player.isGrounded:
        #TODO: remove jump keybind
        Player.move_jump(tt)
    if keys[pygame.K_s]:
        if SURPRISE.get_num_channels() < 1 and DEV_MODE:
            SURPRISE.play() # REPLACE WITH DOG FUNCTION LINKED TO MOVEMENT + SOUND
            Level.num += 1
        
        
    
    #Accelerate if moving left/right
    if keys[pygame.K_a]:
        Player.move_left(tt)
    elif keys[pygame.K_d]:
        Player.move_right(tt)
    elif Player.isGrounded:
        Player.acceleration.x = 0
    
    pygame.draw.rect(screen, "green", Player.rect, 2)
    pygame.draw.rect(screen, "blue", Dog.rect, 2)
    
    #TODO: move this stuff into Character.update and call it here instead
    Player.update(dt, tt)
    Dog.update(dt, tt, Level.total[Level.num])

    if keys[pygame.K_e]:
        Player.move_climb(maxGroup(pygame.sprite.spritecollide(Player, test_level, False),pygame.sprite.spritecollide(Player, test_level, False)),tt)

    collisions(Player, Level.total[Level.num], E_key=keys[pygame.K_e])
    
    match Level.num:
        case 0:
            test_level.draw(screen)
        case 1:
            box_level.draw(screen)
            
    Player.pos = pygame.math.Vector2(Player.rect.center)

    screen.blit(Player.image, Player.rect)
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    tt += 1

pygame.quit()

