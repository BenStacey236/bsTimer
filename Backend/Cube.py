from Methods.generate_scramble import generate_scramble

class Cube():
    def __init__(self):
        # Initialise datastructures for storing cube state (solved to start with)
        self.corners_net = {'a':0,
                        'b':0,
                        'c':0,
                        'd':0,
                        'e':4,
                        'f':4,
                        'g':4,
                        'h':4,
                        'i':1,
                        'j':1,
                        'k':1,
                        'l':1,
                        'm':2,
                        'n':2,
                        'o':2,
                        'p':2,
                        'q':3,
                        'r':3,
                        's':3,
                        't':3,
                        'u':5,
                        'v':5,
                        'w':5,
                        'x':5}
        self.edges_net = {'a':0,
                        'b':0,
                        'c':0,
                        'd':0,
                        'e':4,
                        'f':4,
                        'g':4,
                        'h':4,
                        'i':1,
                        'j':1,
                        'k':1,
                        'l':1,
                        'm':2,
                        'n':2,
                        'o':2,
                        'p':2,
                        'q':3,
                        'r':3,
                        's':3,
                        't':3,
                        'u':5,
                        'v':5,
                        'w':5,
                        'x':5}

        self.scramblestr = ''


    def D(self):
        'Simulates a bottom layer (D) move on the cube'
        
        # Establish the swaps for the permutation
        corner_swaps = zip([i for i in 'uvwxlkpotshg'], [self.corners_net[i] for i in 'xuvwhglkpots'])
        edges_swaps = zip([i for i in 'uvwxkosg'], [self.edges_net[i] for i in 'xuvwgkos'])

        # Perform the permutation to turn the face
        for swap in list(corner_swaps): self.corners_net[swap[0]] = swap[1]
        for swap in list(edges_swaps): self.edges_net[swap[0]] = swap[1]


    def U(self):
        'Simulates a top layer (U) move on the cube'

        # Establish the swaps for the permutation
        corner_swaps = zip([i for i in 'abcdijmnqref'], [self.corners_net[i] for i in 'dabcmnqrefij'])
        edges_swaps = zip([i for i in 'abcdimqe'], [self.edges_net[i] for i in 'dabcmqei'])

        # Perform the permutation to turn the face
        for swap in list(corner_swaps): self.corners_net[swap[0]] = swap[1]
        for swap in list(edges_swaps): self.edges_net[swap[0]] = swap[1]


    def R(self):
        'Simulates a right layer (R) move on the cube'

        # Establish the swaps for the permutation
        corner_swaps = zip([i for i in 'mnopkjcbqtwv'], [self.corners_net[i] for i in 'pmnowvkjcbqt'])
        edges_swaps = zip([i for i in 'mnopjbtv'], [self.edges_net[i] for i in 'pmnovjbt'])

        # Perform the permutation to turn the face
        for swap in list(corner_swaps): self.corners_net[swap[0]] = swap[1]
        for swap in list(edges_swaps): self.edges_net[swap[0]] = swap[1]


    def L(self):
        'Simulates a left layer (L) move on the cube'

         # Establish the swaps for the permutation
        corner_swaps = zip([i for i in 'efghlidarsxu'], [self.corners_net[i] for i in 'hefgdarsxuli'])
        edges_swaps = zip([i for i in 'efghldrx'], [self.edges_net[i] for i in 'hefgdrxl'])

        # Perform the permutation to turn the face
        for swap in list(corner_swaps): self.corners_net[swap[0]] = swap[1]
        for swap in list(edges_swaps): self.edges_net[swap[0]] = swap[1]


    def F(self):
        'Simulates a front layer (F) move on the cube'

         # Establish the swaps for the permutation
        corner_swaps = zip([i for i in 'ijkldcmpvugf'], [self.corners_net[i] for i in 'lijkgfdcmpvu'])
        edges_swaps = zip([i for i in 'ijklcpuf'], [self.edges_net[i] for i in 'lijkfcpu'])

        # Perform the permutation to turn the face
        for swap in list(corner_swaps): self.corners_net[swap[0]] = swap[1]
        for swap in list(edges_swaps): self.edges_net[swap[0]] = swap[1]


    def B(self):
        'Simulates a back layer (B) move on the cube'

         # Establish the swaps for the permutation
        corner_swaps = zip([i for i in 'qrstbaehxwon'], [self.corners_net[i] for i in 'tqrsonbaehxw'])
        edges_swaps = zip([i for i in 'qrstahwn'], [self.edges_net[i] for i in 'tqrsnahw'])

        # Perform the permutation to turn the face
        for swap in list(corner_swaps): self.corners_net[swap[0]] = swap[1]
        for swap in list(edges_swaps): self.edges_net[swap[0]] = swap[1]


    def scramble(self):
        'Scrambles the cube and returns the scramble in cube notationx as a string'

        scramble = generate_scramble()
        scramble = generate_scramble(scramble)
        scramble = generate_scramble(scramble)
        scramble = generate_scramble(scramble)
        scramblestr = ''

        for move in scramble:
            match move:
                case 1:
                    self.L()
                    scramblestr += 'L '
                case 2:
                    self.R()
                    scramblestr += 'R '
                case 3:
                    self.U()
                    scramblestr += 'U '
                case 4:
                    self.D()
                    scramblestr += 'D '
                case 5:
                    self.F()
                    scramblestr += 'F '
                case 6:
                    self.B()
                    scramblestr += 'B '
                case 7:
                    for i in range(0, 3): self.L()
                    scramblestr += "L' "
                case 8:
                    for i in range(0, 3): self.R()
                    scramblestr += "R' "
                case 9:
                    for i in range(0, 3): self.U()
                    scramblestr += "U' "
                case 10:
                    for i in range(0, 3): self.D()
                    scramblestr += "D' "
                case 11:
                    for i in range(0, 3): self.F()
                    scramblestr += "F' "
                case 12:
                    for i in range(0, 3): self.B()
                    scramblestr += "B' "
                case 13:
                    self.L()
                    self.L()
                    scramblestr += "L2 "
                case 14:
                    self.R()
                    self.R()
                    scramblestr += "R2 "
                case 15:
                    self.U()
                    self.U()
                    scramblestr += "U2 "
                case 16:
                    self.D()
                    self.D()
                    scramblestr += "D2 "
                case 17:
                    self.F()
                    self.F()
                    scramblestr += "F2 "
                case 18:
                    self.B()
                    self.B()
                    scramblestr += "B2 "

        self.scramblestr = scramblestr