import pygame

'''
TODO: finish this

add the image to the platform
figure out how to store states
implement class into Constants
'''
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