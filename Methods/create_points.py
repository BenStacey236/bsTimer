import numpy as np

THIRD = 1/3

def create_points(points: list):
    '''Creates the vertices of the cube and appends it to points.'''

    points.append(np.matrix([-1, -1, 1])) # Corner
    points.append(np.matrix([1, -1, 1])) # Corner

    points.append(np.matrix([-THIRD, -1, 1])) # Mid Edge
    points.append(np.matrix([THIRD, -1, 1])) # Mid Edge

    points.append(np.matrix([1, 1, 1])) # Corner
    points.append(np.matrix([-1, 1, 1])) # Corner

    points.append(np.matrix([THIRD, 1, 1])) # Mid Edge
    points.append(np.matrix([-THIRD, 1, 1])) # Mid Edge

    points.append(np.matrix([-1, -1, -1])) # Corner
    points.append(np.matrix([1, -1, -1])) # Corner

    points.append(np.matrix([-THIRD, -1, -1])) # Mid Edge
    points.append(np.matrix([THIRD, -1, -1])) # Mid Edge

    points.append(np.matrix([1, 1, -1])) # Corner
    points.append(np.matrix([-1, 1, -1])) # Corner

    points.append(np.matrix([THIRD, 1, -1])) # Mid Edge
    points.append(np.matrix([-THIRD, 1, -1])) # Mid Edge

    points.append(np.matrix([1, THIRD, -1])) # Mid Edge
    points.append(np.matrix([-1, THIRD, -1])) # Mid Edge
    points.append(np.matrix([1, THIRD, 1])) # Mid Edge
    points.append(np.matrix([-1, THIRD, 1])) # Mid Edge

    points.append(np.matrix([1, -THIRD, -1])) # Mid Edge
    points.append(np.matrix([-1, -THIRD, -1])) # Mid Edge
    points.append(np.matrix([1, -THIRD, 1])) # Mid Edge
    points.append(np.matrix([-1, -THIRD, 1])) # Mid Edge

    points.append(np.matrix([1, 1, -THIRD])) # Mid Edge
    points.append(np.matrix([-1, 1, -THIRD])) # Mid Edge
    points.append(np.matrix([-1, -1, -THIRD])) # Mid Edge
    points.append(np.matrix([1, -1, -THIRD])) # Mid Edge

    points.append(np.matrix([1, 1, THIRD])) # Mid Edge
    points.append(np.matrix([-1, 1, THIRD])) # Mid Edge
    points.append(np.matrix([-1, -1, THIRD])) # Mid Edge
    points.append(np.matrix([1, -1, THIRD])) # Mid Edge

    # Red Face
    points.append(np.matrix([1, THIRD, THIRD])) # Mid Centre
    points.append(np.matrix([1, THIRD, -THIRD])) # Mid Centre
    points.append(np.matrix([1, -THIRD, -THIRD])) # Mid Centre
    points.append(np.matrix([1, -THIRD, THIRD])) # Mid Centre

    # Orange Face
    points.append(np.matrix([-1, THIRD, THIRD])) # Mid Centre
    points.append(np.matrix([-1, THIRD, -THIRD])) # Mid Centre
    points.append(np.matrix([-1, -THIRD, -THIRD])) # Mid Centre
    points.append(np.matrix([-1, -THIRD, THIRD])) # Mid Centre

    # Green Face
    points.append(np.matrix([THIRD, THIRD, 1])) # Mid Centre
    points.append(np.matrix([-THIRD, THIRD, 1])) # Mid Centre
    points.append(np.matrix([-THIRD, -THIRD, 1])) # Mid Centre
    points.append(np.matrix([THIRD, -THIRD, 1])) # Mid Centre

    # Blue Face
    points.append(np.matrix([THIRD, THIRD, -1])) # Mid Centre
    points.append(np.matrix([-THIRD, THIRD, -1])) # Mid Centre
    points.append(np.matrix([-THIRD, -THIRD, -1])) # Mid Centre
    points.append(np.matrix([THIRD, -THIRD, -1])) # Mid Centre

    # Yellow Face
    points.append(np.matrix([THIRD, 1, THIRD])) # Mid Centre
    points.append(np.matrix([-THIRD, 1, THIRD])) # Mid Centre
    points.append(np.matrix([-THIRD, 1, -THIRD])) # Mid Centre
    points.append(np.matrix([THIRD, 1, -THIRD])) # Mid Centre

    # White Face
    points.append(np.matrix([THIRD, -1, THIRD])) # Mid Centre
    points.append(np.matrix([-THIRD, -1, THIRD])) # Mid Centre
    points.append(np.matrix([-THIRD, -1, -THIRD])) # Mid Centre
    points.append(np.matrix([THIRD, -1, -THIRD])) # Mid Centre

    return points