# Example file showing a circle moving on screen
import pygame
import pygame.math as pgm
from CharacterClass import Character
from Constants import *
from level import test_level

'''
ISSUES: 
'p' state platforms colisions don't work properly
'''

#Helper function for collision. 

def collisions(Colidee : Character, Collidergroup : pygame.sprite.Group, RemoveColliderfromList : bool = False,):
    
    collisionslist = pygame.sprite.spritecollide(Colidee, Collidergroup, RemoveColliderfromList)
    
    for thing in collisionslist:
        if thing.state != 'u': # uncollidable
            
            if thing.state == 's': # solid
                #(Colidee.rect.bottom - thing.rect.top)
                #(Colidee.rect.top - thing.rect.bottom)
                if max((Colidee.rect.bottom - thing.rect.top),(Colidee.rect.top - thing.rect.bottom)) <= max((Colidee.rect.left - thing.rect.right),(Colidee.rect.right - thing.rect.left)):
                    if (Colidee.rect.bottom - thing.rect.top) < (Colidee.rect.top - thing.rect.bottom):
                        Colidee.rect.top = thing.rect.bottom
                        Colidee.velocity.y = 0
                    else:
                        Colidee.rect.bottom = thing.rect.top
                        Colidee.velocity.y = 0
                        Colidee.isGrounded = True
                else:
                    if (Colidee.rect.left - thing.rect.right) < (Colidee.rect.right - thing.rect.left):
                        Colidee.rect.left = thing.rect.right
                        Colidee.velocity.x = 0
                    else: # this else handles literally every collision, even if all else fails, so make it an elif.
                        Colidee.rect.right = thing.rect.left
                        Colidee.velocity.x = 0
                #VERY IMPORTANT: Updating the datatype Character 's rect must be done while updating it's pos or else MAJOR consequences
                Colidee.pos = pygame.math.Vector2(Colidee.rect.center)

            elif thing.state == 'p': # partially solid
                if max((Colidee.rect.bottom - thing.rect.top),(Colidee.rect.top - thing.rect.bottom)) >= max((Colidee.rect.left - thing.rect.right),(Colidee.rect.right - thing.rect.left)):
                    if (Colidee.rect.bottom - thing.rect.top) > (Colidee.rect.top - thing.rect.bottom):
                        Colidee.rect.bottom = thing.rect.top
                        Colidee.velocity.y = 0
                        Colidee.isGrounded = True
                        # I DIDN'T TEST THIS. I GOT NO CLUE IF IT WORKS. | It won't work. the edges of the platform would be able to be passed through occasionally. Also the condition is not made for coming from the bottom
                Colidee.pos = pygame.math.Vector2(Colidee.rect.center)
            """
            elif (Colidee.rect.bottom - Colidee.velocity.y) > thing.rect.top: #if partially solid and was above previosely
                print("hi")
                #if they are falling + if their bottom is lower than the top, then:
                Colidee.rect.bottom = thing.rect.top
                Colidee.velocity.y = 0
                Colidee.isGrounded = True"""
            
    return Colidee.rect.copy()



# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

font = pygame.font.SysFont(None, 30)


Player = Character(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 0.2, pgm.Vector2(0,0), pgm.Vector2(0,0), 5)


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
    
    text_surface = font.render(f"Acceleration: {Player.acceleration} | Velocity: {Player.velocity} | Grounded: {Player.isGrounded}", True, (255, 255, 255)) #text on screen
    text_rect = text_surface.get_rect() #size of text
    text_rect.center = (400, 150) #position of text
    screen.blit(text_surface, text_rect) #push text to screen
    


    keys = pygame.key.get_pressed()
    mod_keys = pygame.key.get_mods()

    
    
    if keys[pygame.K_w] and Player.isGrounded:
        #TODO: remove jump keybind
        Player.move_jump()
    if keys[pygame.K_s]:
        print("hi")
        #either crouching or something else idk
        
    
    #Accelerate if moving left/right
    if keys[pygame.K_a]:
        Player.move_left()
    elif keys[pygame.K_d]:
        Player.move_right()
    elif Player.isGrounded:
        Player.acceleration.x = 0
    
    if (Player.acceleration.y < gravity and not Player.isGrounded):
       Player.acceleration.y += 0.1
    
    
    
    pygame.draw.rect(screen, "green", Player.rect, 2)
    
    #TODO: move this stuff into Character.update and call it here instead
    Player.velocity += Player.acceleration * (dt+1)
    
    Player.velocity.y = min(Player.velocity.y, terminal_velocity)
    Player.velocity.x = max(-Player.maxspeed, min(Player.velocity.x, Player.maxspeed))
    
    
    
    Player.pos += Player.velocity
    Player.rect.center = (int(Player.pos.x), int(Player.pos.y)) # safer conversion
    
    Player.isGrounded = False


    test_level.draw(screen)
    Player.rect = collisions(Player, test_level)

    Player.pos = pygame.math.Vector2(Player.rect.center)
    
    #add velocity to acceleration
    
    if Player.acceleration.x == 0:
        Player.velocity.x *= friction #decellerate if not moving (acceleration = 0)
    if 0.1 >= Player.velocity.x and Player.velocity.x >= -0.1 and Player.acceleration.x == 0:
        Player.velocity.x = 0 #set to 0 at small numbers to eliminate scientific configuration Ex. 1.273 * e^10
    
    
    
    screen.blit(Player.image, Player.rect)
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

