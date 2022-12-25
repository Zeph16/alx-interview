#!/usr/bin/python3
'''
Returns a pascal triangle
'''


def pascal_triangle(num):
    ''' Returns a pascal triangle '''
    p_tri = []
    if num <= 0:
        return p_tri
    for i in range(num):
        p_tri.append([])
        p_tri[i].append(1)
        for j in range(1, i):
            p_tri[i].append(p_tri[i - 1][j - 1] + p_tri[i - 1][j])
        if i > 0:
            p_tri[i].append(1)
    return p_tri
