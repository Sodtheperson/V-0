import pygame



pygame.display.set_mode((1280, 720))
class Platform(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int,int], image : str | tuple[int,int,int], state : str = 's', width: None | int =None, height: None | int =None, isDoor: bool | None = None):
        super().__init__()

        if isinstance(image, str): # if it is a string
            self.image = pygame.image.load(image).convert_alpha() 
        elif not (width is None) or not (height is None):
            self.image = pygame.Surface((float(width), float(height)))  # create a blank surface
            self.image.fill(image) # fill it with the color, which is in the place of image
        else:
            raise ValueError("Error in Platform Constructor: image and (width or height) were None")
        
        self.imagecolor = image
        self.rect = self.image.get_rect(topleft=pos)
        self.pos = pos # stores the position of the top left pixel
        self.isDoor = isDoor

        # s is solid
        # p is partially solid (only the top collision)
        # u is uncolidable
        if state in ["s","p","u"]:
            self.state = state
        else:
            raise ValueError("Error in Platform Constructor: invalid state type")
    
    def __str__(self):
        return "platform at " + str(self.pos) + " with state " + str(self.state)
    
class Button(Platform):
    local_frame_check = 0
    def __init__(self, pos: tuple[int,int], image : str | tuple[int,int,int], width: None | int =None, height: None | int =None):
        super().__init__(pos, image, state='u', width=width, height=height)
        self.pressed = False
        self.was_colliding = False
        self.base_pos = pos

        self.base_image = self.image
        self.pressed_image = pygame.transform.scale(self.base_image, (self.rect.width, int(self.rect.height * 0.5)))
    def update(self):
        print(self.pressed)
        self.local_frame_check = 1
        if self.pressed:
            self.image = self.pressed_image
            self.pos = pygame.math.Vector2(self.base_pos[0], self.base_pos[1] + self.rect.height)
            self.rect = self.image.get_rect(topleft=self.pos)
            # we need to change it from tuples to pygame.vector2 so i can reassign position (though, theres probably a better way of doing this)
        else:
            self.pos = self.base_pos
            self.rect = self.image.get_rect(topleft=self.pos)
            self.image = self.base_image