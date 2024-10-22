from AppAssets.AppPresets import *

from Methods.format_time import format_time


class SolveBlock:
    def __init__(self, solve_number:int, solve_time:float, scramblestr:str, ao3_time, ao5_time, ao12_time, ao100_time):
        'Initialises the values passed in and renders the text ready for drawing'

        self.solve_number = solve_number
        self.solve_time = solve_time
        self.scramblestr = scramblestr
        
        # Ensures that the block can only be clicked when it is being rendered
        self.drawn = False

        # Stores the solve time and each average for that solve
        # If no average passed then set to a blank dash
        self.solve_time = format_time(solve_time)
        if not type(ao3_time) == str: self.ao3_time = format_time(ao3_time)
        else: self.ao3_time = '      -'
        if not type(ao5_time) == str: self.ao5_time = format_time(ao5_time)
        else: self.ao5_time = '      -'
        if not type(ao12_time) == str: self.ao12_time = format_time(ao12_time)
        else: self.ao12_time = '      -'
        if not type(ao100_time) == str: self.ao100_time = format_time(ao100_time)
        else: self.ao100_time = '      -'

        # Renders text ready for drawing
        self.number_text = SOLVES_FONT.render(str(self.solve_number), True, BASICALLY_WHITE)
        self.time_text = SOLVES_FONT.render(str(self.solve_time), True, BASICALLY_WHITE)
        self.ao3_text = SOLVES_FONT.render(str(self.ao3_time), True, BASICALLY_WHITE)


    def draw(self, surface:pygame.surface, total_solves:int, offset=0):
        'Draws the solve block to the screen'
        
        # Calculate the coordinate of the solve block taking into account 
        # the offset from scrolling
        self.coordinate = (21, 232+(total_solves-self.solve_number)*40+20+40*round(offset))

        # Get PyGame rect objects to draw the text at the correct location
        self.solve_number_text_rect = self.number_text.get_rect(center=self.coordinate)
        self.solve_time_text_rect = self.time_text.get_rect(midleft=(49, self.coordinate[1]))
        self.ao3_text_rect = self.ao3_text.get_rect(midleft=(135, self.coordinate[1]))

        # Only draws to the screen if the block is within the sidebar to 
        # prevent unnecessary strain on the rendering process
        if self.coordinate[1] > 232 and self.coordinate[1] < surface.get_height(): 
            surface.blit(self.number_text, self.solve_number_text_rect)
            surface.blit(self.time_text, self.solve_time_text_rect)
            surface.blit(self.ao3_text, self.ao3_text_rect)

            pygame.draw.line(surface, LIGHT_GREY, (0, self.coordinate[1]+17), (215, self.coordinate[1]+17))
            pygame.draw.line(surface, LIGHT_GREY, (0, self.coordinate[1]-23), (215, self.coordinate[1]-23))
            self.drawn = True
        else:
            self.drawn = False


    def is_clicked(self, mouse_pos):
        'Returns True if the SolveBlock is clicked and it is being drawn'

        if self.drawn and (self.solve_number_text_rect.collidepoint(mouse_pos) or self.solve_time_text_rect.collidepoint(mouse_pos) or self.ao3_text_rect.collidepoint(mouse_pos)):
            return True