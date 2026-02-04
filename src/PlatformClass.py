import pygame
'''
TODO: finish this

add the image to the platform
figure out how to store states
implement class into Constants
'''

# Minor thing: 
# https://www.geeksforgeeks.org/python/pygame-creating-sprites/
# this is just an example of sprite classes, but also
# making a sprite also creates a rect object for it            <- then why did you add self.rect?
# so we could use the sprite's rect instead of making one here
# and since sprites can have images, that would solve the image issue too
# plus it would also still be a platform class we can index in the floors list,
# so we can check states on it 

# TLDR: use sprites instead of making new rects since it solves image + rect and keeps states.
class Platform(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int,int], image : str | None, state : str = 's', width: None | int =None, height: None | int =None):
        super().__init__()

        if isinstance(image, str): # if it is a string
            self.image = pygame.image.load(image).convert_alpha() 
        elif not width is None or not height is None:
            self.image = pygame.Surface((width, height))  # create a blank surface
            self.image.fill(image) # fill it with the color, which is in the place of image
        else:
            raise ValueError("Error in Platform Constructor: image and (width or height) were None")
        
        self.rect = self.image.get_rect()
        self.pos = pos # stores the position of the top left pixel

        # s is solid
        # p is partially solid (only the top collision)
        # u is uncolidable
        if state in ["s","p","u"]:
            self.state = state
        else:
            raise ValueError("Error in Platform Constructor: invalid state type")
#




