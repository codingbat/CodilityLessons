#!/usr/bin/python

'''
Created on 17 Oct 2015

@author: Nazmul Alam
'''

class TapeEquilibrium:
    def __init__(self):
        self.data = []
    
    def solution(self, A):
        lowest = 0
        leftSum = A[0]
        rightSum = 0
        for x in range(1, len(A)-1):
            leftSum += A[x]
            rightSum = self.rightsum(x, A)
            #print leftSum, rightSum 
            #print x
            if x == 1:
                lowest = abs(leftSum - rightSum)
            if (abs(leftSum-rightSum) < lowest):
                lowest = abs(leftSum - rightSum)
            
        return lowest
    
    def rightsum(self, p, A):
        total = 0
        for p in range(p, len(A)):
            total += A[p]
        return total
    
    def efficient(self, A):
        leftsum = A[0]
        rightsum = sum(A[x] for x in range(1, len(A)))
        min_dif = abs(leftsum - rightsum)
        for x in range(1, len(A)-1):
            leftsum += A[x]
            rightsum -= A[x]
            if abs(leftsum - rightsum) < min_dif:
                min_dif = abs(leftsum - rightsum)
        return min_dif