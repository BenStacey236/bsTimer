import pygame
from overrides import override

from UI.Button import Button


class ScrambleButton(Button):
    def is_hovering(self):
        'Iterates the frame index for animation when pressed'

        mouse_pos = pygame.mouse.get_pos()
        
        if self.button_rect.collidepoint(mouse_pos):
            self.frame_index += 1
            if self.frame_index == len(self.frames): self.frame_index = self.frame_multiplier
        else:
            self.frame_index = 0


    @override
    def is_clicked(self):
        'Returns a boolean value based on if the button is clicked or not'

        self.is_hovering()
        mouse_pos = pygame.mouse.get_pos()
        
        # Detects if the buttons is clicked and returns True
        if pygame.mouse.get_pressed()[0] and self.button_rect.collidepoint(mouse_pos):
            if not self.clicked:
                self.clicked = True
                return True
            
        # Returns False if not clicked
        else:
            self.clicked = False
            return False