import time
import math

from Backend.Cube import Cube
from Methods.format_time import format_time


class Solve():
    def __init__(self, current_cube:Cube=None):
        'Initialses default parameters for a solve'
        
        # Creates a new cube object if one is not passed
        if current_cube == None:
            self.cube = Cube()
            self.cube.scramble()
        else:
            self.cube = current_cube

        self.start_time = 0
        self.end_time = 0
        self.solving = False
        self.time_text = '00:00:00'
        self.solved = False
    
    
    def start_solve(self):
        'Starts the solve by recording the start time'

        self.start_time = time.perf_counter()
        self.solving = True


    def end_solve(self):
        'Ends the solve by recording the end time and returning the solve time'

        self.end_time = time.perf_counter()
        self.solving = False
        self.solved = True
        self.update_time()

        return self.end_time - self.start_time


    def update_time(self):
        'Updates the elapsed solve time since the start of the solve'
        
        if self.solving:
            solve_time = time.perf_counter() - self.start_time
            self.time_text = f'{format_time(solve_time):0>8}'