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
class Platforms(pygame.sprite.Sprite):
    def __init__(self, x, y, image : str | tuple, state : str = 'solid', width=None, height=None):
        super().__init__()

        self.image = pygame.image.load(image).convert_alpha() 
        if image != str: # if it isnt a string, ergo not an image.png,
            self.image = pygame.Surface((width, height))  # create a blank surface
            self.image.fill(image) # fill it with the color, which is in the place of image

        self.rect = self.image.get_rect() < and then it defines the rect
        self.text.x = x
        self.text.y = y
        self.state = state

        


    Rewrote to use sprites instead of rects, remove the comments if you wanna incorperate.
    I also added stuff into main.py for collision checking with states.
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