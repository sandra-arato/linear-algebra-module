#!/usr/bin/python
import math
from decimal import Decimal, getcontext

getcontext().prec = 30
CANNOT_NORMALIZE_ZERO = 'Cannot normalize the zero vector'

class Vector(object):

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
    return Decimal(math.sqrt(sum(lengthSq)))

def normalize(a):
    length = magnitude(a)
    vector = scalar(a, (1 / length))
    return vector

def innerPr(a, b):
    product = 0
    multiplied = [x * y for x, y in zip(a.coordinates, b.coordinates)]
    for s in multiplied:
        product += s
    return product

def angleRad(a,b):
    product = innerPr(a, b)
    magnitudeProduct = magnitude(a) * magnitude(b)
    cos = product / magnitudeProduct
    return math.acos(cos)

def angleDeg(a, b):
    rad = angleRad(a, b)
    return math.degrees(rad)
