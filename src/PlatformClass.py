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