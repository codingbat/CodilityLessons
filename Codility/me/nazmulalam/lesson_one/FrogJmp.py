'''
Created on 20 Nov 2015

@author: Naz
'''
import math
def solution(X, Y, D):
    distance = Y - D
    return int(math.floor(distance/D)+1)