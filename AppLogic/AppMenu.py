import pygame
from overrides import override

from AppAssets.AppPresets import *
from AppLogic.BaseApp import BaseApp
from UI.Button import Button


class AppMenu(BaseApp):
    def __init__(self, surface, WIDTH=1000, HEIGHT=800):
        # Initialise Default Perimeters for the PyGame Window
        self.WIN = surface
        self.running = True
        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT

        # Initialise Buttons
        self.timerapp_button = Button(['MenuButton2DBase', 'MenuButton2DClicked'], (self.__WIDTH/2-379-40, 120))
        self.app3d_button = Button(['MenuButton3DBase', 'MenuButton3DClicked'], (self.__WIDTH/2+40, 120))


    def handle_buttons(self):
        'Handles the logic for button presses'

        if self.timerapp_button.is_clicked():
            return True
        
        if self.app3d_button.is_clicked():
            return False

        return None


    @override
    def draw_window(self):
        'Draws the UI to the screen'
        
        self.WIN.fill(GREY)

        # Draw Buttons
        self.timerapp_button.draw(self.WIN)
        self.app3d_button.draw(self.WIN)
        
        pygame.display.update()


    @override
    def app_tick(self):
        'Handles all of the app logic on each tick'

        for event in pygame.event.get():
            # Quits application if 'X' button on the window is pressed
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN:
                # Quits application if escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    exit()

        # After all logic for tick has been handled, window is drawn
        self.draw_window()

        return self.handle_buttons()