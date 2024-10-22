import pygame

from AppAssets.AppPresets import *
from Backend.Cube import Cube


class Face():
    def __init__(self, current_cube:Cube, projected_points:list, point1:int, point2:int, point3:int, point4:int, letter:str, corner = True):
        'Initialises the colour of the face and its vertices to be drawn at'

        self.letter = letter
        self.colours = {0:WHITE, 1:GREEN, 2:RED, 3:BLUE, 4:ORANGE, 5:YELLOW}
        
        # Sets the colour of the face using the correct net array based on
        # whether or not the face is on a corner piece or edge piece
        if corner:
            self.colour = self.colours[current_cube.corners_net[self.letter]]
        else:
            self.colour = self.colours[current_cube.edges_net[self.letter]]
        
        # Coordinates of the 4 corners of the face, taken from projected_points
        self.tl = projected_points[point1]    # Top left coordinate
        self.bl = projected_points[point2]    # Bottom left coordinate
        self.tr = projected_points[point3]    # Top right coordinate
        self.br = projected_points[point4]    # Bottom right coordinate
    

    def draw(self, surface:pygame.surface):
        'Draws the face to the screen'

        pygame.draw.polygon(surface, self.colour, [self.tl, self.bl, self.tr, self.br])
