from math import sqrt, acos, degrees, pi
#from decimal import Decimal, getcontext

#getcontext().prec = 30

class Vector(object):

    CANNNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            #self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)
            self.in_degrees = False

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
	        # Vector * scalar
            #new_coordinates = [x * Decimal(other) for x in self.coordinates]
            new_coordinates = [x * other for x in self.coordinates]
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
        #return Decimal(sqrt(sum(coordinates_squared)))
        return sqrt(sum(coordinates_squared))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            #return self * (Decimal('1.0') / magnitude)
            return self * (1. / magnitude)

        except ZeroDivisionError:
            raise Exception(self.CANNNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def __xor__(self, other):
        try:
            # Vector ^ Vector
            #dot_mult = self.__mul__(other)
            #magnitude_mult = self.magnitude() * other.magnitude()
            #if self.in_degrees or other.in_degrees:
            #    return degrees(acos( dot_mult / magnitude_mult ))
            #else:
            #    return acos( dot_mult / magnitude_mult )
            u1 = self.normalized()
            u2 = other.normalized()
            angle_in_radians = acos(u1.__mul__(u2))

            if self.in_degrees or other.in_degrees:
                return degrees(angle_in_radians)
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot find angle with a zero vector')
            else:
                raise e

    def is_parallel_with(self, other):
        return self.__mul__(other) == 0

    def is_orthogonal_with(self, other):
        if self.__mul__(other) == 0:
            return True
        angle = round(self.__xor__(other), 2)
        return angle == 0.00 or angle == round(pi, 2)
