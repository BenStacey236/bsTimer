import random

def generate_scramble(scramble:list = None):
    '''Method that generates a validated, 20 move long array of numbers
       that will be used to scramble a cube object'''
       
    new_scramble = scramble if scramble != None else [random.randint(1, 12) for x in range(1, 20)]
    
    for index, move in enumerate(new_scramble):
        # Check to see if the current move is the inverse of the previous
        # If it is it replaces the current move with a new random one
        if move == (new_scramble[index-1]+6) or move == (new_scramble[index-1]-6): new_scramble[index] = random.randint(1, 12)
        
        # If three consecutive moves are the same, then they are replaced
        # With the X' form, and two moves are added to the scramble
        # E.g L, R, R, R --> L, R', F, B
        if index < len(new_scramble) - 2:
            if move == new_scramble[index+1] and move == new_scramble[index+2]: 
                if move < 7: new_scramble[index] = move + 7
                elif move < 13: new_scramble[index] = move - 7
                new_scramble.pop(index+1)
                new_scramble.pop(index+2)
                new_scramble.append(random.randint(1, 12))
                new_scramble.append(random.randint(1, 12))

        # If two consecutive moves are the same, then they are replaced
        # with the X2 form, and another move is added to the scramble
        # E.g L, R, R, F --> L, R2, F, B
        if index < len(new_scramble) - 1:
            if move == new_scramble[index+1]: 
                if move < 7: new_scramble[index] = move + 12
                else: new_scramble[index] = move + 6
                new_scramble.pop(index+1)
                new_scramble.append(random.randint(1, 12))

    return new_scramble