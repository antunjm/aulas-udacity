from math import sqrt, acos

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
        #return 'Vector: {}'.format(self.coordinates)
        return '(' + ', '.join(format(f, '.3f') for f in self.coordinates) + ')'

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
        #new_coordinates = []
        #for i in range(self.dimension):
        #    new_coordinates.append(self.coordinates[i] + v.coordinates[i])
        #return Vector(new_coordinates)
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)        

    def __sub__(self, other):
        #new_coordinates = []
        #for i in range(self.dimension):
        #    new_coordinates.append(self.coordinates[i] - other.coordinates[i])
        #return Vector(new_coordinates)        
        new_coordinates = [x-y for x,y in zip(self.coordinates, other.coordinates)]
        return Vector(new_coordinates)

    def __rsub__(self, other):
        if other == 0:
            return self
        else:
            return self.__sub__(other)        

    def __mul__(self, other):
        if type(other) is Vector:
            # dot product
            coordinates_mul = [x*y for x,y in zip(self.coordinates, other.coordinates)]
            return sum(coordinates_mul)
        else:
            new_coordinates = [x*other for x in self.coordinates]
            return Vector(new_coordinates)

    def __rmul__(self, other):
        if other == 0:
            return self
        else:
            return self.__mul__(other)        

    def magnitude(self):
        #soma = 0
        #for i in range(self.dimension):
        #    soma = soma + math.pow(self.coordinates[i], 2)
        #return sqrt(soma)
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self * (1. / magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def angle(self, other):
        dot_mult = self.__mul__(other)
        magnitude_mult = self.magnitude() * other.magnitude()
        return acos( dot_mult / magnitude_mult )
