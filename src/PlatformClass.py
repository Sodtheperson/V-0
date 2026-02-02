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
# making a sprite also creates a rect object for it
# so we could use the sprite's rect instead of making one here
# and since sprites can have images, that would solve the image issue too
# plus it would also still be a platform class we can index in the floors list,
# so we can check states on it 

# TLDR: use sprites instead of making new rects since it solves image + rect and keeps states.
"""
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height]) < image stuff, we can shift to loading an image from assets
        self.image.fill(SURFACE_COLOR) < this is just color for if we arent doing that
        self.image.set_colorkey(COLOR) < same for above

        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height)) < we can use this as the rect

        self.rect = self.image.get_rect() < and then it defines the rect
        
        # we could also add state here, then add the appending to the list after.


    Stole this from the link from before
"""

# we also have to add some form of forced stage loading soon because making pixel-precise flooring
# is gonna suck if we have to go through the entire level every time just to get to the one we need to test
# but thats for a later problem

class Platform(pygame.Rect):
    def __init__ (self, left, top, width, height, state):
        super().__init__(left, top, width, height)
        self.state = state
        return
    def __init__ (self, top_left, size, state):
        super().__init__(top_left, size)
        self.state = state
        return
    def __init__ (self, object, state):
        super().__init__(object)
        self.state = state
        return