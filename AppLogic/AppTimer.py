import pygame
import time
from overrides import override

pygame.init()

from AppAssets.AppPresets import *
from AppLogic.BaseApp import BaseApp
from Backend.Cube import Cube
from Backend.Solve import Solve
from Backend.SolvingSession import SolvingSession
from Methods.format_time import format_time
from UI.Button import Button
from UI.NetFace import NetFace
from UI.PopWindow import PopWindow
from UI.ScrambleButton import ScrambleButton
from UI.SolveBlock import SolveBlock
from UI.TextBox import TextBox


class AppTimer(BaseApp):
    def __init__(self, current_cube:Cube, surface:pygame.surface, FPS:int, WIDTH=1000, HEIGHT=800, session_name='Default Session'):
        # Sets the app perameters based on the passed arguments
        self.WIN = surface
        self.current_cube = current_cube
        self.running = True
        self.current_solve = Solve(self.current_cube)
        self.current_session = SolvingSession(session_name)
        self.current_session.load_solves()

        self.__WIDTH = WIDTH
        self.__HEIGHT = HEIGHT

        # Initialising Text
        self.timer_text = TIMER_FONT_2D.render('00:00:00', True, WHITE)
        self.scramble_text = SCRAMBLE_FONT.render(self.current_cube.scramblestr, True, BASICALLY_WHITE)
        self.mean_text = SOLVES_TITLE_FONT.render(f'Mean Time: {format_time(self.current_session.mean)}', True, BASICALLY_WHITE)
        self.fastest_text = SOLVES_TITLE_FONT.render(f'Best Time: {format_time(self.current_session.fastest_time)}', True, BASICALLY_WHITE)
        self.num_solves_text = SOLVES_TITLE_FONT.render(f'No. Solves: {self.current_session.num_solves}', True, BASICALLY_WHITE)
        
        # Initialising variables
        self.popwindows = []
        self.offset = 0
        self.timer_colour = WHITE
        self.solve_time = -1
        self.held = False
        self.shift = False
        self.countdown = 0
        
        # Buttons and text boxes
        self.scramble_button = ScrambleButton(['ScrambleButtonBase', 'ScrambleButtonF1', 'ScrambleButtonF2', 'ScrambleButtonF3', 'ScrambleButtonF4'], (self.__WIDTH-230, 80), int(8//(60/FPS)))
        self.session_input = TextBox(5, 78, session_name)
        self.change_view_button = Button(['ChangeView3DButtonBase','ChangeView3DButtonClicked'], (self.__WIDTH/2-85 ,self.__HEIGHT-110))

        if len(self.current_session.solves) > 0: 
            self.solve_number = self.current_session.solves[-1][0] + 1
        else:
            self.solve_number = 1


    def handle_buttons(self):
        'Handles the logic for button functions when they are pressed'

        if self.scramble_button.is_clicked():
            self.current_solve = Solve()
            self.current_cube = self.current_solve.cube

        if self.change_view_button.is_clicked():
            return True

        for window in self.popwindows:
            if window.close_button.is_clicked():
                self.popwindows = []
            
            elif window.delete_button.is_clicked():
                self.solve_number -= 1
                if self.solve_number < 1: self.solve_number = 1
                self.current_session.delete_solve(window.solve_number)
                self.current_session.load_solves()
                self.popwindows = []


    def handle_keypress(self, key:pygame.key):
        'Handles keypresses during application runtime'

        if key == pygame.K_LSHIFT: self.shift = True
        
        if self.session_input.selected:
            self.session_input.input_key(key, self.shift)
        
        if self.current_solve.solving:
            self.current_session.insert_solve(self.solve_number, self.current_solve.end_solve(), self.current_solve.cube.scramblestr)
            
            self.solve_number += 1
            self.current_session.load_solves()

        if key == pygame.K_SPACE:
            if not self.held:
                self.countdown = time.perf_counter()

            self.held = True
            if not self.current_solve.solving and not self.session_input.selected: self.timer_colour = RED


    def handle_keyrelease(self, key:pygame.key):
        'Handles release of keys during application runtime'
        
        if key == pygame.K_LSHIFT: self.shift = False
        
        # Logic for changing timer colour and starting the solve if space held for 1 second
        if key == pygame.K_SPACE:
            self.held = False
            if time.perf_counter() - self.countdown > 1:
                self.current_solve.start_solve()
                self.timer_colour = WHITE
            else:
                self.countdown = 0
                self.timer_colour = WHITE


    def handle_scroll(self, y:int, max:int):
        'Handles mouse scrolling during application runtime'
        
        if y > 0:
            self.offset += 0.25
        elif y < 0:
            self.offset -= 0.25

        if self.offset < 14-max: self.offset = (14-max)
        if self.offset > 0 or max < 15: self.offset = 0
    

    def handle_mouse_click(self, mouse_pos:tuple):
        'Handles mouse clicks during application runtime'
        
        # Checks if session input box is clicked
        self.session_input.is_clicked()
        
        # If solve in sidebar is clicked, opens a popup window. 
        if len(self.popwindows) > 1:
            self.popwindows = [self.popwindows[1]]
        for block in self.solve_blocks:
            if block.is_clicked(mouse_pos):
                self.popwindows.append(PopWindow(block.solve_number, block.solve_time, block.scramblestr, block.ao3_time, block.ao5_time, block.ao12_time, block.ao100_time))

        
    def draw_net_face(self, colour:tuple, startx:int, starty:int, letters:list):
        'Draws one face of the cube net with top left at (startx, starty)'
        
        # Draws the centre square
        pygame.draw.polygon(self.WIN, colour, [(startx+30, starty+30), (startx+60, starty+30), (startx+60, starty+60), (startx+30, starty+60)])
        
        # Creates the squares for the corners and edges of the face
        corner_faces = [NetFace((startx, starty), (startx+30, starty), (startx+30, starty+30), (startx, starty+30), letters[0], self.current_solve),
                        NetFace((startx+60, starty), (startx+90, starty), (startx+90, starty+30), (startx+60, starty+30), letters[1], self.current_solve),
                        NetFace((startx+60, starty+60), (startx+90, starty+60), (startx+90, starty+90), (startx+60, starty+90), letters[2], self.current_solve),
                        NetFace((startx, starty+60), (startx+30, starty+60), (startx+30, starty+90), (startx, starty+90), letters[3], self.current_solve)]

        edge_faces = [NetFace((startx+30, starty), (startx+60, starty), (startx+60, starty+30), (startx+30, starty+30), letters[0], self.current_solve, False),
                      NetFace((startx+60, starty+30), (startx+90, starty+30), (startx+90, starty+60), (startx+60, starty+60), letters[1], self.current_solve, False),
                      NetFace((startx+30, starty+60), (startx+60, starty+60), (startx+60, starty+90), (startx+30, starty+90), letters[2], self.current_solve, False),
                      NetFace((startx, starty+30), (startx+30, starty+30), (startx+30, starty+60), (startx, starty+60), letters[3], self.current_solve, False)]

        # Draws the squares for the corners and edges of the face
        for square in corner_faces:
            square.draw(self.WIN)

        for square in edge_faces:
            square.draw(self.WIN)

        # Draws the outlines
        pygame.draw.polygon(self.WIN, BLACK, [(startx, starty), (startx+90, starty), (startx+90, starty+90), (startx, starty+90)], 2)
        pygame.draw.line(self.WIN, BLACK, (startx+30, starty), (startx+30, starty+90))
        pygame.draw.line(self.WIN, BLACK, (startx+60, starty), (startx+60, starty+90))
        pygame.draw.line(self.WIN, BLACK, (startx, starty+30), (startx+90, starty+30))
        pygame.draw.line(self.WIN, BLACK, (startx, starty+60), (startx+90, starty+60))


    @override
    def draw_window(self):
        'Draws the UI to the screen'
        
        self.WIN.fill(GREY)

        # Draw timer regardless
        self.timer_text = TIMER_FONT_2D.render(self.current_solve.time_text, True, self.timer_colour)
        self.WIN.blit(self.timer_text, (self.__WIDTH/2-175, self.__HEIGHT/2-30))

        if not self.current_solve.solving: # Everthing apart from timer dissapears when solving
            
            # Drawing background colour blocks and lines
            pygame.draw.polygon(self.WIN, LIGHT_GREY, [(0, 0), (self.__WIDTH, 0), (self.__WIDTH, 70), (0, 70)])
            pygame.draw.polygon(self.WIN, V_LIGHT_GREY, [(0, 70), (215, 70), (215, self.__HEIGHT), (0, self.__HEIGHT)])
            
            pygame.draw.line(self.WIN, LIGHT_GREY, (0, 192), (215, 192), 2) # Top of sidebar grid
            pygame.draw.line(self.WIN, LIGHT_GREY, (42, 192), (42, self.__HEIGHT), 2) # Sidebar vertical line
            pygame.draw.line(self.WIN, LIGHT_GREY, (128, 192), (128, self.__HEIGHT), 2) # Sidebar vertical line
            pygame.draw.line(self.WIN, LIGHT_GREY, (215, 70), (215, self.__HEIGHT), 3)
            pygame.draw.line(self.WIN, GREY, (0, 70), (self.__WIDTH, 70), 3)
        
        
            # Drawing the cube net
            self.draw_net_face(WHITE, self.__WIDTH-300, self.__HEIGHT-300, ['a', 'b', 'c', 'd'])
            self.draw_net_face(ORANGE, self.__WIDTH-395, self.__HEIGHT-205, ['e', 'f', 'g', 'h'])
            self.draw_net_face(GREEN, self.__WIDTH-300, self.__HEIGHT-205, ['i', 'j', 'k', 'l'])
            self.draw_net_face(RED, self.__WIDTH-205, self.__HEIGHT-205, ['m', 'n', 'o', 'p'])
            self.draw_net_face(BLUE, self.__WIDTH-110, self.__HEIGHT-205, ['q', 'r', 's', 't'])
            self.draw_net_face(YELLOW, self.__WIDTH-300, self.__HEIGHT-110, ['u', 'v', 'w', 'x'])
            
            # Render text
            self.timer_text = TIMER_FONT_2D.render(self.current_solve.time_text, True, self.timer_colour)
            self.scramble_text = SCRAMBLE_FONT.render(self.current_cube.scramblestr, True, BASICALLY_WHITE)
            self.grid_title = SOLVES_TITLE_FONT.render(' #    Time       AO3', True, BASICALLY_WHITE)
            self.mean_text = SOLVES_TITLE_FONT.render(f'Mean Time: {format_time(self.current_session.mean)}', True, BASICALLY_WHITE)
            self.fastest_text = SOLVES_TITLE_FONT.render(f'Best Time: {format_time(self.current_session.fastest_time)}', True, BASICALLY_WHITE)
            self.num_solves_text = SOLVES_TITLE_FONT.render(f'No. Solves: {self.current_session.num_solves}', True, BASICALLY_WHITE)
            self.time_difference_text = SOLVES_TITLE_FONT.render(('+' if self.current_session.time_difference > 0 else '')+format_time(self.current_session.time_difference), True, RED if self.current_session.time_difference > 0 else GREEN)
        
            # Draw text
            scramble_text_rect = self.scramble_text.get_rect(center=(self.__WIDTH/2, 40))
            time_difference_text_rect = self.time_difference_text.get_rect(center=(self.__WIDTH/2, self.__HEIGHT/2+65))

            self.WIN.blit(self.timer_text, (self.__WIDTH/2-175, self.__HEIGHT/2-30))
            self.WIN.blit(self.time_difference_text, time_difference_text_rect)
            self.WIN.blit(self.scramble_text, scramble_text_rect)
            self.WIN.blit(self.num_solves_text, (4, 110))
            self.WIN.blit(self.fastest_text, (10, 137))
            self.WIN.blit(self.mean_text, (1, 164))
            self.WIN.blit(self.grid_title, (8, 202))
        
            # Draw Buttons and Text Boxes
            self.scramble_button.draw(self.WIN)
            self.change_view_button.draw(self.WIN)
            self.session_input.draw(self.WIN)

            # Draw Solves list in sidebar
            self.solve_blocks = []
            for index, solve in enumerate(self.current_session.solves):
                ao3, ao5, ao12, ao100 = '', '', '', ''
                if solve[0] > 99: ao100 = sum(self.current_session.solves[index-i][1] for i in range(0, 100))/100
                if solve[0] > 11: ao12 = sum(self.current_session.solves[index-i][1] for i in range(0, 12))/12
                if solve[0] > 4: ao5 = sum(self.current_session.solves[index-i][1] for i in range(0, 5))/5
                if solve[0] > 2: ao3 = sum(self.current_session.solves[index-i][1] for i in range(0, 3))/3

                todraw = SolveBlock(solve[0], solve[1], solve[2], ao3, ao5, ao12, ao100)
                todraw.draw(self.WIN, len(self.current_session.solves), self.offset)
                
                self.solve_blocks.append(todraw)

            for window in self.popwindows:
                window.draw(self.WIN)

        pygame.display.update()


    @override
    def app_tick(self):
        'Handles all of the app logic on each tick'

        # Updates the solve time if a solve is in progress
        if self.current_solve.solving: self.current_solve.update_time()

        # Turns the timer green if the spacebar has been held for 1 second
        if time.perf_counter() - self.countdown > 1 and self.held: self.timer_colour = GREEN
        
        # If the change view button is pressed, then returns true so application
        # can be switched in the main program
        if self.handle_buttons(): return True

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

                # Handles the logic for any other keypresses
                self.handle_keypress(event.key)

            # Handles the logic for any keys released
            if event.type == pygame.KEYUP:
                self.handle_keyrelease(event.key)

            # Adjusts the offset for the sidebar depending on if the mouse is scrolled
            max = len(self.current_session.solves)
            if event.type == pygame.MOUSEWHEEL:
                self.handle_scroll(event.y, max)

            # Handles mouse clicks
            if pygame.mouse.get_pressed()[0]:
                self.handle_mouse_click(pygame.mouse.get_pos())

        # Changes the current session if the text input box is changed
        if self.session_input.saved_text != self.current_session.session_name:
            self.current_session = SolvingSession(self.session_input.saved_text)
            self.current_session.load_solves()
            if len(self.current_session.solves) > 0: 
                self.solve_number = self.current_session.solves[-1][0] + 1
            else:
                self.solve_number = 1
            self.offset = 0
        
        # After all logic for tick has been handled, window is drawn
        self.draw_window()
