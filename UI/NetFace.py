import pygame

from AppAssets.AppPresets import *
from Backend.Solve import Solve


class NetFace:
    def __init__(self, point1:tuple, point2:tuple, point3:tuple, point4:tuple, letter:str, current_solve:Solve, corner = True):
        'Initialises the colour of the face and its vertices to be drawn at'

        # Sets the colour of the face using the correct net array based on
        # whether or not the face is on a corner piece or edge piece
        self.letter = letter
        self.colours = {0:WHITE, 1:GREEN, 2:RED, 3:BLUE, 4:ORANGE, 5:YELLOW}
        if corner:
            self.colour = self.colours[current_solve.cube.corners_net[self.letter]]
        else:
            self.colour = self.colours[current_solve.cube.edges_net[self.letter]]

        # Coordinates of the 4 corners of the face, taken from points passed in
        self.tl = point1   # Top left coordiinate
        self.bl = point2   # Bottom left coordinate
        self.tr = point3   # Top right coordinate
        self.br = point4   # Bottom right coordinate


    def draw(self, surface:pygame.surface):
        'Draws the face to the screen'

        pygame.draw.polygon(surface, self.colour, [self.tl, self.bl, self.tr, self.br])