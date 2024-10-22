import pygame

from Backend.Cube import Cube
from AppLogic.App3D import App3D
from AppLogic.AppTimer import AppTimer
from AppLogic.AppMenu import AppMenu

pygame.init()

# Initialises the constants and creates pygame window
FPS = 120
WIDTH, HEIGHT = 1000, 800
pygame.display.set_caption("BSTimer")
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

current_cube = Cube()
current_app = AppMenu(WIN, WIDTH, HEIGHT)
 

def switch_app(current_app):
    'Method that switches between the Timer and 3D apps'

    if isinstance(current_app, App3D):
        current_app = AppTimer(current_app.current_cube, WIN, FPS, WIDTH, HEIGHT, current_app.current_session.session_name)
    
    elif isinstance(current_app, AppTimer):
        current_app = App3D(current_app.current_cube, WIN, FPS, WIDTH, HEIGHT, current_app.current_session.session_name)

    return current_app


if __name__ == '__main__':
    clock = pygame.time.Clock()
    
    while current_app.running:
        clock.tick(FPS)
        
        # Switches from the Menu to the app who's button is pressed
        if isinstance(current_app, AppMenu):
            if current_app.app_tick() == True:
                current_app = AppTimer(current_cube, WIN, FPS, WIDTH, HEIGHT)
            
            elif current_app.app_tick() == False:
                current_app = App3D(current_cube, WIN, FPS, WIDTH, HEIGHT)

        if current_app.app_tick():
            current_app = switch_app(current_app)