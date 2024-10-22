import pygame

from AppAssets.AppPresets import *
from UI.Button import Button


class PopWindow:
    def __init__(self, solve_number:int, solve_time:float, scramblestr:str, ao3_time:float, ao5_time:float, ao12_time:float, ao100_time:float):
        'Initialises the text and buttons that are shown in the window'

        # Initialises all of the text shown on the window 
        self.solve_number = solve_number
        self.solve_time = solve_time
        if scramblestr == '': self.scramblestr = 'Custom Scramble'
        else: self.scramblestr = scramblestr
        self.ao3_time = ao3_time
        self.ao5_time = ao5_time
        self.ao12_time = ao12_time
        self.ao100_time = ao100_time

        # Initialises buttons for the window
        self.delete_button = Button(['DeleteButtonBase', 'DeleteButtonClicked'], (440, 467))
        self.close_button = Button(['CloseButtonBase', 'CloseButtonClicked'], (671, 305))

        # Renders text ready to be drawn to screen
        self.number_text = SOLVES_TITLE_FONT.render(f'#{str(self.solve_number)}', True, BASICALLY_WHITE)
        self.time_text = SOLVES_TITLE_FONT.render(f'Time: {str(self.solve_time)}', True, BASICALLY_WHITE)
        self.scramble_text = SOLVES_FONT.render(str(self.scramblestr), True, BASICALLY_WHITE)
        self.ao3_text = SOLVES_FONT.render(f'ao3: {str(self.ao3_time)}', True, BASICALLY_WHITE)
        self.ao5_text = SOLVES_FONT.render(f'ao5: {str(self.ao5_time)}', True, BASICALLY_WHITE)
        self.ao12_text = SOLVES_FONT.render(f'ao12: {str(self.ao12_time)}', True, BASICALLY_WHITE)
        self.ao100_text = SOLVES_FONT.render(f'ao100: {str(self.ao100_time)}', True, BASICALLY_WHITE)


    def draw(self, surface:pygame.surface):
        'Draws the window to the screen including buttons and text'

        pygame.draw.polygon(surface, V_LIGHT_GREY, [(300, 300), (700, 300), (700, 500), (300, 500)])

        # Get PyGame rects so that text can be drawn in the correct place
        self.scramble_text_rect = self.scramble_text.get_rect(midtop=(surface.get_width()/2, 340))
        self.time_text_rect = self.time_text.get_rect(midtop=(surface.get_width()/2, 310))

        # Draw buttons
        self.delete_button.draw(surface)
        self.close_button.draw(surface)

        # Draw text to the screen
        surface.blit(self.number_text, (310, 310))
        surface.blit(self.time_text, self.time_text_rect)
        surface.blit(self.ao3_text, (360, 380))
        surface.blit(self.ao5_text, (540, 380))
        surface.blit(self.ao12_text, (353, 420))
        surface.blit(self.ao100_text, (517, 420))
        surface.blit(self.scramble_text, self.scramble_text_rect)
