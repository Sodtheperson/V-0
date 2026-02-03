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


Player = Character(pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2), 0.2, pgm.Vector2(0,0), pgm.Vector2(0,0), 5)
Player.acceleration.y = 1
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
        
    
    if keys[pygame.K_a]:
        Player.move_left()
    elif keys[pygame.K_d]:
        Player.move_right()
    elif Player.isGrounded:
        Player.acceleration.x = 0
    
    if (Player.acceleration.y < gravity and not Player.isGrounded):
       Player.acceleration.y += 0.1
    
    
      
    #Accelerate if moving left/right
    prev_rect = Player.rect.copy()
    
    pygame.draw.rect(screen, "green", Player.rect, 2)
    pygame.draw.rect(screen, "red", prev_rect, 2)
    
    Player.velocity += Player.acceleration
    
    Player.velocity.y = min(Player.velocity.y, terminal_velocity)
    
    Player.velocity.x = max(-Player.maxspeed, min(Player.velocity.x, Player.maxspeed))
    
    
    
    Player.pos += Player.velocity
    Player.rect.center = Player.pos
    
    Player.isGrounded = False
    """"
    rendered_platforms = pygame.sprite.Group()

    ground = Platforms(0, 500, 1000, 50, "ground.png", 'solid')
    rendered_platforms.add(ground)

    collisions = pygame.sprite.spritecollide(Player, rendered_platforms, False)
    for platform in collisions:
        if platform.state == 'solid':
            # we take the info from below
        elif platform.state == 'passthrough':
            # do nothing
        elif platform.state == 'semisolid':
            # only top has collision
        elif platform.state == 'box':
            # pushable box example-- still gotta figure that out.


    rendered_platforms.draw(screen) # we draw all the platforms that are currently supposed to be rendered 
    # should move this to constants, and append there to have consistency.
    """
    for floor in floors:
        pygame.draw.rect(screen, "green", floor)
        if Player.rect.colliderect(floor) and Player.velocity.y > 0 and prev_rect.bottom <= floor.top:
            Player.rect.bottom = floor.top
            Player.pos.y = Player.rect.centery
            Player.velocity.y = 0
            Player.isGrounded = True
        if Player.rect.colliderect(floor) and prev_rect.bottom <= floor.top: 
            ## What if we replace it with a double indexing dictionary that can hold passthrough rectangles vs solid vs alternates? (vent entrances, etc.)
            print("HI")
            Player.rect.top = floor.bottom
            Player.isGrounded = True
            Player.pos.y = Player.rect.centery
    
    #add velocity to acceleration
    
    if Player.acceleration.x == 0:
        Player.velocity.x *= friction #decellerate if not moving (acceleration = 0)
    if 0.1 >= Player.velocity.x and Player.velocity.x >= -0.1 and Player.acceleration.x == 0:
        Player.velocity.x = 0 #set to 0 at small numbers to eliminate scientific configuration Ex. 1.273 * e^10
        

    
        
    Player.pos.x += Player.velocity.x * dt
    
    
    screen.blit(Player.image, Player.rect)
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

