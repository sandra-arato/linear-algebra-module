import math
class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

def add(a, b):
    new_coordinates = [x + y for x, y in zip(a.coordinates, b.coordinates)]
    vector = Vector(new_coordinates)
    return vector

def subtract(a, b):
    new_coordinates = [x - y for x, y in zip(a.coordinates, b.coordinates)]
    vector = Vector(new_coordinates)
    return vector

def scalar(a, scale):
    coordinates = [coordinate * scale for coordinate in a.coordinates ]
    vector = Vector(coordinates)
    return vector

def magnitude(a):
    lengthSq = [math.pow(x, 2) for x in a.coordinates] 
    return math.sqrt(sum(lengthSq))

def normalize(a):
    length = magnitude(a)
    vector = scalar(a, (1 / length))
    return vector


