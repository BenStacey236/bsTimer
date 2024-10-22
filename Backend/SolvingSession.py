import sqlite3 as sq
import math


class SolvingSession:
    def __init__(self, session_name:str):
        '''Sets up the database connection and intitialises an empty table in the
           correct format if the specified file does not already contain this table'''

        self.session_name = session_name
        self.solves = []
        self.__connection = sq.connect(f'Sessions/{self.session_name}.db')
        self.__cursor = self.__connection.cursor()

        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS solves (
            solve_number INTEGER PRIMARY KEY,
            solve_time FLOAT,
            scramble TEXT)""")
        
        self.__connection.commit()


    def load_solves(self):
        'Loades the solves stored in the database and stores it in self.solves'

        self.__cursor.execute("""
        SELECT * FROM solves""")

        results = self.__cursor.fetchall()

        self.solves = []
        for solve in results:
            self.solves.append(solve)

        self.calculate_mean()
        self.get_fastest()
        self.num_solves = len(self.solves)
        self.get_difference()
    

    def insert_solve(self, solve_number:int, solve_time:float, scramble:str):
        'Inserts a record with the given parameters into the database'
        
        self.__cursor.execute(f"""
        INSERT INTO solves VALUES
        ({solve_number}, {solve_time}, "{scramble}")""")

        self.__connection.commit()


    def delete_solve(self, solve_number:int):
        '''Deletes the solve with the given solve number from the database\n
           Reassigns the solve numbers to ensure no gaps in the database'''

        self.__cursor.execute(f"""
        DELETE FROM solves
        WHERE solve_number = {solve_number}""")
                
        self.__connection.commit()

        self.load_solves()

        self.__cursor.execute(f"""
        DELETE FROM solves""")

        for index, solve in enumerate(self.solves):
            self.insert_solve(index+1, solve[1], solve[2])


    def calculate_mean(self):
        'Calculates the mean solve time in the session'

        total = 0
        for solve in self.solves: total += solve[1]

        if len(self.solves) > 0: self.mean = total/len(self.solves)
        else: self.mean = 0

    
    def get_fastest(self):
        'Calculates the fastest time in the session'
        
        fastest = math.inf
        for solve in self.solves:
            if solve[1] < fastest:
                fastest = solve[1]

        if fastest == math.inf: self.fastest_time = 0
        else: self.fastest_time = fastest

    
    def get_difference(self):
        'Calculates the time difference between the last two solves'

        if self.num_solves > 1:
            self.time_difference = self.solves[-1][1]-self.solves[-2][1]
        
        else:
            self.time_difference = 0