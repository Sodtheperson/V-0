import pygame



pygame.display.set_mode((1280, 720))
class Platform(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int,int], image : str | tuple[int,int,int], state : str = 's', width: None | int =None, height: None | int =None):
        super().__init__()

        if isinstance(image, str): # if it is a string
            self.image = pygame.image.load(image).convert_alpha() 
        elif not (width is None) or not (height is None):
            self.image = pygame.Surface((float(width), float(height)))  # create a blank surface
            self.image.fill(image) # fill it with the color, which is in the place of image
        else:
            raise ValueError("Error in Platform Constructor: image and (width or height) were None")
        
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pos # stores the position of the top left pixel

        # s is solid
        # p is partially solid (only the top collision)
        # u is uncolidable
        if state in ["s","p","u"]:
            self.state = state
        else:
            raise ValueError("Error in Platform Constructor: invalid state type")
    
    def __str__(self):
        return "platform at " + str(self.pos) + "with state" + str(self.state)