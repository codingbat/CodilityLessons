'''
Created on 20 Nov 2015

@author: Naz
'''
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import math
def solution(A, B):
    # write your code in Python 2.7
    array = []
    for i in range(0, len(A)):
        array.append(int(combinations(A[i], B[i])))
    return array
    
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fibIter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    next = 0
    first = 0
    second = 1
    for i in range(0, n):
        next = first + second
        first = second
        second = next
    return next
    
    
def combinations(i, j):
    return  fibIter(i) % math.pow(2, j)