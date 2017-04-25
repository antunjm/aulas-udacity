#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

"""
Udacity - aulas
"""
from vector import Vector

if __name__ == '__main__':
    
    """
    # Quiz 1
    print('Quiz 1:')
    v1 = Vector([8.218, -9.341])
    v2 = Vector([-1.129, 2.111])
    print('{} + {} = {}'.format(v1, v2, v1 + v2))

    v1 = Vector([7.119, 8.215])
    v2 = Vector([-8.223, 0.878])
    print('{} - {} = {}'.format(v1, v2, v1 - v2))

    scalar = 7.41
    v = Vector([1.671, -1.012, -0.318])
    print('{} * {:.3f} = {}'.format(v, scalar, v * scalar))
    

    # Quiz 2
    print('Quiz 2:')
    v = Vector([-0.221, 7.437])
    print('1) {} magnitude={:.3f}'.format(v, v.magnitude()))

    v = Vector([8.813, -1.331, -6.247])
    print('2) {} magnitude={:.3f}'.format(v, v.magnitude()))

    v = Vector([5.581, -2.136])
    print('3) {} normalized={}'.format(v, v.normalized()))

    v = Vector([1.996, 3.108, -4.554])
    print('4) {} normalized={}'.format(v, v.normalized()))

    v = Vector([0, 0])
    print('extra) {} magnitude={:.3f}'.format(v, v.magnitude()))
    """
    # Quiz 3
    print('Quiz 3:')

    v1 = Vector([7.887, 4.138])
    v2 = Vector([-8.802, 6.776])
    print('1) {} . {} = {:.3f}'.format(v1, v2, v1 * v2))

    v1 = Vector([-5.955, -4.904, -1.874])
    v2 = Vector([-4.496, 8.802, 6.776])
    print('2) {} . {} = {:.3f}'.format(v1, v2, v1 * v2))

    v1 = Vector([1, 2, -1])
    v2 = Vector([3, 1, 0])
    print('exemple) {} . {} = {:.3f}'.format(v1, v2, v1 * v2))
    print(v1.magnitude())
    print(v2.magnitude())
    #print(v1.angle(v2))
    print(v1 ^ v2)
