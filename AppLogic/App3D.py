import numpy as np
import pygame
from math import *
from overrides import override

from AppAssets.AppPresets import *
from AppLogic.BaseApp import BaseApp
from Backend.Cube import Cube
from Backend.Solve import Solve
from Backend.SolvingSession import SolvingSession
from Methods.create_points import create_points
from UI.Button import Button
from UI.Face import Face
from UI.ScrambleButton import ScrambleButton

pygame.init()

# Initialises the projection matrix
PROJECTION_MATRIX = np.matrix([[1, 0, 0],
                               [0, 1, 0]])


class App3D(BaseApp):
    def __init__(self, current_cube:Cube, surface:pygame.surface, FPS:int, WIDTH=1000, HEIGHT=800, session_name = 'Default Session'):
        # Sets the app perameters based on the passed arguments
        self.WIN = surface
        self.current_cube = current_cube
        self.current_solve = Solve(current_cube)
        self.current_session = SolvingSession(session_name)
        self.running = True
        
        # Initialses constant values for the UI
        self.__HEIGHT = HEIGHT
        self.__WIDTH = WIDTH
        self.__SCALE = 130
        self.__CENTRE_OFFSET = [WIDTH/2, HEIGHT/2]

        # Initialises the default perameters for cube angle
        self.shift = False
        self.x_angle = -0.59
        self.y_angle = -0.26
        self.circle_x_angle = 326.1635
        self.circle_y_angle = 345.089
        self.previous_x = None
        self.previous_y = None

        self.points = []
        create_points(self.points)
        
        # Creates placeholder values for the projected points array
        self.projected_points = [[n, n] for n in range(len(self.points))]

        # Creates an empty stack for undoing moves
        self.recent_moves = []

        # Initialise Text
        self.timer_text = TIMER_FONT_3D.render('00:00:00', True, WHITE)

        # Initialise Buttons
        self.scramble_button = ScrambleButton(['ScrambleButtonBase', 'ScrambleButtonF1', 'ScrambleButtonF2', 'ScrambleButtonF3', 'ScrambleButtonF4'], (self.__WIDTH-230, 10), int(8//(60/FPS)))
        self.change_view_button = Button(['ChangeView2DButtonBase','ChangeView2DButtonClicked'], (self.__WIDTH/2-85 ,self.__HEIGHT-110))


    def connect_points(self, i:int, j:int, points:list, colour = BLACK):
        'Draws a line between the points at index "i" and "j" in the "points" array'

        pygame.draw.line(self.WIN, colour, (points[i][0], points[i][1]), (points[j][0], points[j][1]), 2)


    def draw_red(self):
        'Draws the side of the cube surrounding the red centre piece'

        # Draws the centre piece as this never changes position
        pygame.draw.polygon(self.WIN, RED, [self.projected_points[32], self.projected_points[33], self.projected_points[34], self.projected_points[35]]) # Red Centre
        
        # Defines the Face objects with their parameters and which location on the cube they are displaying 
        corner_faces = [Face(self.current_cube, self.projected_points, 1, 31, 35, 22, 'm'),
                        Face(self.current_cube, self.projected_points, 27, 9, 20, 34, 'n'),
                        Face(self.current_cube, self.projected_points, 33, 16, 12, 24, 'o'),
                        Face(self.current_cube, self.projected_points, 18, 32, 28, 4, 'p')]

        edge_faces = [Face(self.current_cube, self.projected_points, 31, 27, 34, 35, 'm', False),
                      Face(self.current_cube, self.projected_points, 34, 33, 16, 20, 'n', False),
                      Face(self.current_cube, self.projected_points, 32, 33, 24, 28, 'o', False),
                      Face(self.current_cube, self.projected_points, 22, 35, 32, 18, 'p', False)]

        # Draws the Faces to the screen
        for square in corner_faces:
            square.draw(self.WIN)

        for square in edge_faces:
            square.draw(self.WIN)

        # Draws the outlining lines on the red centre side
        self.connect_points(1, 4, self.projected_points)
        self.connect_points(1, 9, self.projected_points)
        self.connect_points(4, 12, self.projected_points)
        self.connect_points(9, 12, self.projected_points)
        self.connect_points(16, 18, self.projected_points)
        self.connect_points(20, 22, self.projected_points)
        self.connect_points(24, 27, self.projected_points)
        self.connect_points(28, 31, self.projected_points)


    def draw_orange(self):
        'Draws the side of the cube surrounding the orange centre piece'

        # Draws the centre piece as this never changes position
        pygame.draw.polygon(self.WIN, ORANGE, [self.projected_points[36], self.projected_points[37], self.projected_points[38], self.projected_points[39]]) # Orange Centre
        
        # Defines the Face objects with their parameters and which location on the cube they are displaying
        corner_faces = [Face(self.current_cube, self.projected_points, 8, 26, 38, 21, 'e'),
                        Face(self.current_cube, self.projected_points, 30, 0, 23, 39, 'f'),
                        Face(self.current_cube, self.projected_points, 36, 19, 5, 29, 'g'),
                        Face(self.current_cube, self.projected_points, 17, 37, 25, 13, 'h')]

        edge_faces = [Face(self.current_cube, self.projected_points, 26, 30, 39, 38, 'e', False),
                      Face(self.current_cube, self.projected_points, 39, 23, 19, 36, 'f', False),
                      Face(self.current_cube, self.projected_points, 37, 36, 29, 25, 'g', False),
                      Face(self.current_cube, self.projected_points, 21, 38, 37, 17, 'h', False)]

        # Draws the Faces to the screen
        for square in corner_faces:
            square.draw(self.WIN)

        for square in edge_faces:
            square.draw(self.WIN)

        # Draws the outlining lines on the orange centre side
        self.connect_points(8, 13, self.projected_points)
        self.connect_points(0, 8, self.projected_points)
        self.connect_points(0, 5, self.projected_points)
        self.connect_points(5, 13, self.projected_points)
        self.connect_points(17, 19, self.projected_points)
        self.connect_points(21, 23, self.projected_points)
        self.connect_points(25, 26, self.projected_points)
        self.connect_points(29, 30, self.projected_points)

    
    def draw_green(self):
        'Draws the side of the cube surrounding the green centre piece'
        
        # Draws the centre piece as this never changes position
        pygame.draw.polygon(self.WIN, GREEN, [self.projected_points[40], self.projected_points[41], self.projected_points[42], self.projected_points[43]]) # Green Centre
        
        # Defines the Face objects with their parameters and which location on the cube they are displaying
        corner_faces = [Face(self.current_cube, self.projected_points, 0, 2, 42, 23, 'i'),
                        Face(self.current_cube, self.projected_points, 3, 1, 22, 43, 'j'),
                        Face(self.current_cube, self.projected_points, 40, 18, 4, 6, 'k'),
                        Face(self.current_cube, self.projected_points, 19, 41, 7, 5, 'l')]

        edge_faces = [Face(self.current_cube, self.projected_points, 3, 2, 42, 43, 'i', False),
                      Face(self.current_cube, self.projected_points, 43, 40, 18, 22, 'j', False),
                      Face(self.current_cube, self.projected_points, 41, 40, 6, 7, 'k', False),
                      Face(self.current_cube, self.projected_points, 23, 42, 41, 19, 'l', False)]

        # Draws the Faces to the screen
        for square in corner_faces:
            square.draw(self.WIN)

        for square in edge_faces:
            square.draw(self.WIN)

        # Draws the outlining lines on the green centre side
        self.connect_points(0, 5, self.projected_points)
        self.connect_points(1, 4, self.projected_points)
        self.connect_points(18, 19, self.projected_points)
        self.connect_points(22, 23, self.projected_points)
        self.connect_points(2, 7, self.projected_points)
        self.connect_points(3, 6, self.projected_points)
        self.connect_points(0, 1, self.projected_points)
        self.connect_points(4, 5, self.projected_points)


    def draw_blue(self):
        'Draws the side of the cube surrounding the blue centre piece'
        
        # Draws the centre piece as this never changes position
        pygame.draw.polygon(self.WIN, BLUE, [self.projected_points[44], self.projected_points[45], self.projected_points[46], self.projected_points[47]]) # Blue Centre
        
        # Defines the Face objects with their parameters and which location on the cube they are displaying
        corner_faces = [Face(self.current_cube, self.projected_points, 9, 11, 47, 20, 'q'),
                        Face(self.current_cube, self.projected_points, 10, 8, 21, 46, 'r'),
                        Face(self.current_cube, self.projected_points, 45, 17, 13, 15, 's'),
                        Face(self.current_cube, self.projected_points, 16, 44, 14, 12, 't')]

        edge_faces = [Face(self.current_cube, self.projected_points, 11, 10, 46, 47, 'q', False),
                    Face(self.current_cube, self.projected_points, 46, 21, 17, 45, 'r', False),
                    Face(self.current_cube, self.projected_points, 44, 45, 15, 14, 's', False),
                    Face(self.current_cube, self.projected_points, 44, 47, 20, 16, 't', False)]

        # Draws the Faces to the screen
        for square in corner_faces:
            square.draw(self.WIN)

        for square in edge_faces:
            square.draw(self.WIN)

        # Draws the outlining lines on the blue centre side
        self.connect_points(8, 13, self.projected_points)
        self.connect_points(9, 12, self.projected_points)
        self.connect_points(11, 14, self.projected_points)
        self.connect_points(10, 15, self.projected_points)
        self.connect_points(8, 9, self.projected_points)
        self.connect_points(12, 13, self.projected_points)
        self.connect_points(16, 17, self.projected_points)
        self.connect_points(20, 21, self.projected_points)


    def draw_yellow(self):
        'Draws the side of the cube surrounding the yellow centre piece'
        
        # Draws the centre piece as this never changes position
        pygame.draw.polygon(self.WIN, YELLOW, [self.projected_points[48], self.projected_points[49], self.projected_points[50], self.projected_points[51]]) # Yellow Centre
        
        # Defines the Face objects with their parameters and which location on the cube they are displaying
        corner_faces = [Face(self.current_cube, self.projected_points, 5, 7, 49, 29, 'u'),
                        Face(self.current_cube, self.projected_points, 6, 4, 28, 48, 'v'),
                        Face(self.current_cube, self.projected_points, 51, 24, 12, 14, 'w'),
                        Face(self.current_cube, self.projected_points, 25, 50, 15, 13, 'x')]

        edge_faces = [Face(self.current_cube, self.projected_points, 7, 6, 48, 49, 'u', False),
                      Face(self.current_cube, self.projected_points, 48, 28, 24, 51, 'v', False),
                      Face(self.current_cube, self.projected_points, 50, 51, 14, 15, 'w', False),
                      Face(self.current_cube, self.projected_points, 29, 49, 50, 25, 'x', False)]

        # Draws the Faces to the screen
        for square in corner_faces:
            square.draw(self.WIN)

        for square in edge_faces:
            square.draw(self.WIN)

        # Draws the outlining lines on the yellow centre side
        self.connect_points(4, 12, self.projected_points)
        self.connect_points(5, 13, self.projected_points)
        self.connect_points(6, 14, self.projected_points)
        self.connect_points(7, 15, self.projected_points)
        self.connect_points(4, 5, self.projected_points)
        self.connect_points(12, 13, self.projected_points)
        self.connect_points(24, 25, self.projected_points)
        self.connect_points(28, 29, self.projected_points)


    def draw_white(self):
        'Draws the side of the cube surrounding the white centre piece'
        
        # Draws the centre piece as this never changes position
        pygame.draw.polygon(self.WIN, WHITE, [self.projected_points[52], self.projected_points[53], self.projected_points[54], self.projected_points[55]]) # White Centre
        
        # Defines the Face objects with their parameters and which location on the cube they are displaying
        corner_faces = [Face(self.current_cube, self.projected_points, 8, 10, 54, 26, 'a'),
                        Face(self.current_cube, self.projected_points, 11, 9, 27, 55, 'b'),
                        Face(self.current_cube, self.projected_points, 52, 31, 1, 3, 'c'),
                        Face(self.current_cube, self.projected_points, 30, 53, 2, 0, 'd'),]

        edge_faces = [Face(self.current_cube, self.projected_points, 10, 11, 55, 54, 'a', False),
                      Face(self.current_cube, self.projected_points, 55, 52, 31, 27, 'b', False),
                      Face(self.current_cube, self.projected_points, 53, 52, 3, 2, 'c', False),
                      Face(self.current_cube, self.projected_points, 26, 54, 53, 30, 'd', False)]

        # Draws the Faces to the screen
        for square in corner_faces:
            square.draw(self.WIN)
        
        for square in edge_faces:
            square.draw(self.WIN)

        # Draws the outlining lines on the white centre side
        self.connect_points(0, 8, self.projected_points)
        self.connect_points(1, 9, self.projected_points)
        self.connect_points(2, 10, self.projected_points)
        self.connect_points(3, 11, self.projected_points)
        self.connect_points(26, 27, self.projected_points)
        self.connect_points(30, 31, self.projected_points)
        self.connect_points(0, 1, self.projected_points)
        self.connect_points(8, 9, self.projected_points)


    def project_points(self):
        'Projects self.points from [x, y, z] coordinates to [x, y] coordinates in self.projected_points'
        
        i = 0
        for point in self.points:
            # Multiplies point by rotation matrices
            rotated2d = np.dot(self.rotation_y, point.reshape(3, 1))
            rotated2d = np.dot(self.rotation_x, rotated2d)

            # Multiplies point by projectoin matrix to convert to 3D points
            projected2d = np.dot(PROJECTION_MATRIX, rotated2d)

            x = int((projected2d[0][0]) * self.__SCALE) + self.__CENTRE_OFFSET[0] 
            y = int((projected2d[1][0]) * self.__SCALE) + self.__CENTRE_OFFSET[1]
            
            # Assigns points to their corresponding location in projected points
            self.projected_points[i] = [x, y]
            i += 1


    def handle_keypress(self, key:pygame.key):
        'Handles keypresses during application runtime'

        if key == pygame.K_LSHIFT:
            self.shift = True

        if key == pygame.K_r:
            self.current_cube.scramblestr = 'Custom Scramble'
            # Starts the timer if cube scrambled and timer hasnt started
            if not self.current_solve.solving and not self.current_solve.solved: self.current_solve.start_solve()
            
            # If shift is held, anticlockwise rotation, otherwise a clockwise rotation of R
            if self.shift:
                self.recent_moves.append("r'")
                self.current_cube.R()
                self.current_cube.R()
                self.current_cube.R()
            else:
                self.recent_moves.append("r") 
                self.current_cube.R()

        if key == pygame.K_l:
            self.current_cube.scramblestr = 'Custom Scramble'
            # Starts the timer if cube scrambled and timer hasnt started
            if not self.current_solve.solving and not self.current_solve.solved: self.current_solve.start_solve()
            
            # If shift is held, anticlockwise rotation, otherwise a clockwise rotation of L
            if self.shift:
                self.recent_moves.append("l'")
                self.current_cube.L()
                self.current_cube.L()
                self.current_cube.L()
            else:
                self.recent_moves.append("l")
                self.current_cube.L()
        
        if key == pygame.K_f:
            self.current_cube.scramblestr = 'Custom Scramble'
            # Starts the timer if cube scrambled and timer hasnt started
            if not self.current_solve.solving and not self.current_solve.solved: self.current_solve.start_solve()
            
            # If shift is held, anticlockwise rotation, otherwise a clockwise rotation of F
            if self.shift:
                self.recent_moves.append("f'")
                self.current_cube.F()
                self.current_cube.F()
                self.current_cube.F()
            else:
                self.recent_moves.append("f")
                self.current_cube.F()
        
        if key == pygame.K_b:
            self.current_cube.scramblestr = 'Custom Scramble'
            # Starts the timer if cube scrambled and timer hasnt started
            if not self.current_solve.solving and not self.current_solve.solved: self.current_solve.start_solve()
            
            # If shift is held, anticlockwise rotation, otherwise a clockwise rotation of B
            if self.shift:
                self.recent_moves.append("b'")
                self.current_cube.B()
                self.current_cube.B()
                self.current_cube.B()
            else:
                self.recent_moves.append("b") 
                self.current_cube.B()
        
        if key == pygame.K_d:
            self.current_cube.scramblestr = 'Custom Scramble'
            # Starts the timer if cube scrambled and timer hasnt started
            if not self.current_solve.solving and not self.current_solve.solved: self.current_solve.start_solve()
            
            # If shift is held, anticlockwise rotation, otherwise a clockwise rotation of D
            if self.shift:
                self.recent_moves.append("d'")
                self.current_cube.D()
                self.current_cube.D()
                self.current_cube.D()
            else: 
                self.recent_moves.append("d")
                self.current_cube.D()
        
        if key == pygame.K_u:
            self.current_cube.scramblestr = 'Custom Scramble'
            # Starts the timer if cube scrambled and timer hasnt started
            if not self.current_solve.solving and not self.current_solve.solved: self.current_solve.start_solve()
            
            # If shift is held, anticlockwise rotation, otherwise a clockwise rotation of U
            if self.shift:
                self.recent_moves.append("u'")
                self.current_cube.U()
                self.current_cube.U()
                self.current_cube.U()
            else: 
                self.recent_moves.append("u")
                self.current_cube.U()

        if key == pygame.K_BACKSPACE:
            self.handle_undo()


    def handle_buttons(self):
        'Handles the logic for button functions when they are pressed'
        
        if self.scramble_button.is_clicked():
            self.current_cube.scramble()
            self.current_solve = Solve(self.current_cube)
        
        if self.change_view_button.is_clicked():
            return True


    def handle_keyrelease(self, key:pygame.key):
        'Handles logic for when a key is released'
        
        if key == pygame.K_LSHIFT:
            self.shift = False


    def handle_mouse_movement(self):
        'Handles mouse movement at app runtime'
        
        SENSITIVITY = 57.35

        # Determines how much the mouse has moved in the x direction
        if self.previous_x == None: self.previous_x = pygame.mouse.get_pos()[0]
        current_x = pygame.mouse.get_pos()[0]
        x_change, self.previous_x = current_x - self.previous_x, current_x

        # Determines how much the mouse has moved in the y direction
        if self.previous_y == None: self.previous_y = pygame.mouse.get_pos()[1]
        current_y = pygame.mouse.get_pos()[1]
        y_change, self.previous_y = current_y - self.previous_y, current_y

        # Updates the x and y angles based on the determined movement
        self.x_angle += x_change/100
        self.y_angle -= y_change/100

        # Calculates the circular angle between 0 and 360
        self.circle_x_angle = (self.x_angle*SENSITIVITY)%360
        self.circle_y_angle = (self.y_angle*SENSITIVITY)%360

        # If cube is upside down, adds 180˚ to x circular angle
        if self.circle_y_angle >= 90 and self.circle_y_angle <= 270:
            self.circle_x_angle = (180+self.circle_x_angle)%360
            
            # Inverses mvement in the x direction
            self.x_angle += 2*(-x_change/100)


    def handle_undo(self):
        'Undoes the most recent move on the cube'

        if len(self.recent_moves) > 0:
            previous_move = self.recent_moves[-1]
            match previous_move:
                case 'r': self.current_cube.R(), self.current_cube.R(), self.current_cube.R()
                case 'u': self.current_cube.U(), self.current_cube.U(), self.current_cube.U()
                case 'l': self.current_cube.L(), self.current_cube.L(), self.current_cube.L()
                case 'b': self.current_cube.B(), self.current_cube.B(), self.current_cube.B()
                case 'f': self.current_cube.F(), self.current_cube.F(), self.current_cube.F()
                case 'd': self.current_cube.D(), self.current_cube.D(), self.current_cube.D()
                case "r'": self.current_cube.R()
                case "u'": self.current_cube.U()
                case "l'": self.current_cube.L()
                case "b'": self.current_cube.B()
                case "f'": self.current_cube.F()
                case "d'": self.current_cube.D()

            self.recent_moves.pop(-1)

        else:
            print('No moves left to undo')   
        

    @override
    def draw_window(self):
        'Draws the UI to the screen'
        
        self.WIN.fill(GREY)

        self.project_points()

        # Determines which sides should be drawn to the screen depending on the circular angles
        if self.circle_x_angle >= 0 and self.circle_x_angle < 90:
            self.draw_green()
            self.draw_orange()
        elif self.circle_x_angle >= 90 and self.circle_x_angle < 180:
            self.draw_orange()
            self.draw_blue()
        elif self.circle_x_angle >= 180 and self.circle_x_angle < 270:
            self.draw_blue()
            self.draw_red()
        elif self.circle_x_angle > 270 and self.circle_x_angle <= 360:
            self.draw_red()
            self.draw_green()

        if self.circle_y_angle >= 0 and self.circle_y_angle < 180:
            self.draw_yellow()
        elif self.circle_y_angle >= 180 and self.circle_y_angle <= 360:
            self.draw_white()

        # Draws buttons to the screen
        self.scramble_button.draw(self.WIN)
        self.change_view_button.draw(self.WIN)

        # Renders Timer Text
        self.timer_text = TIMER_FONT_3D.render(self.current_solve.time_text, True, WHITE)
        self.timer_rect = self.timer_text.get_rect(midleft=(self.__WIDTH/2-85, self.__HEIGHT-140))
        self.WIN.blit(self.timer_text, self.timer_rect)

        pygame.display.update()


    @override
    def app_tick(self):
        'Handles all of the app logic on each tick'

        # Max stack size of 50
        if len(self.recent_moves) > 50: self.recent_moves.pop(0)

        # Updates timer if started solve
        self.current_solve.update_time()

        # Stops timer if cube is solved
        if self.current_cube.edges_net == Cube().edges_net and self.current_cube.corners_net == Cube().corners_net:
            self.current_solve.end_solve()

        # Handle all button logic
        if self.handle_buttons(): return True

        # Handles the logic when left click is pressed on the mouse
        if pygame.mouse.get_pressed()[0]:
            self.handle_mouse_movement()

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

            if event.type == pygame.KEYUP:
                # Handles logic when a key is released
                self.handle_keyrelease(event.key)

            # Resets mouse movement when left click isn't pressed
            if event.type == pygame.MOUSEBUTTONUP:
                self.previous_y = None
                self.previous_x = None

        # Updates rotation matrices with the current perspective angles
        self.rotation_x = np.matrix([[1, 0, 0],
                                     [0, cos(self.y_angle), -sin(self.y_angle)],
                                     [0, sin(self.y_angle), cos(self.y_angle)]])

        self.rotation_y = np.matrix([[cos(self.x_angle), 0, sin(self.x_angle)],
                                     [0, 1, 0],
                                     [-sin(self.x_angle), 0, cos(self.x_angle)]])

        # After all logic for tick has been handled, window is drawn
        self.draw_window()