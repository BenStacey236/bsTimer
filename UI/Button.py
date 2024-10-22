import pygame

class Button:
    def __init__(self, frame_files: list, coordinates: tuple, multiplier=1):
        'Initialises the textures as coordinates for the button'
        
        # Frame multiplier handles how many game ticks should be spent displaying each image
        # Default of 1 for a normal button, but can be increased 
        self.frame_multiplier = multiplier
        self.frames = []
        for frame_file in frame_files:
            for i in range(0, self.frame_multiplier): 
                self.frames.append(pygame.image.load(f'AppAssets/{frame_file}.png'))
        
        # Initalises the coordinates and pygame Rect that will be used for detecting button clicks
        self.frame_index = 0
        self.coordinates = coordinates
        self.button_rect = self.frames[self.frame_index].get_rect(topleft=self.coordinates)
        self.clicked = False


    def is_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        
        # Checks if the button has been pressed
        if pygame.mouse.get_pressed()[0] and self.button_rect.collidepoint(mouse_pos):
            self.frame_index = self.frame_multiplier
            self.clicked = True

        elif self.clicked:
            return True

        else:
            self.frame_index = 0
            self.clicked = False


    def draw(self, surface:pygame.surface):
        'Draws the button to the provided surface'
        
        surface.blit(self.frames[self.frame_index], self.coordinates)
        