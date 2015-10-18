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
        leftSum = 0
        rightSum = 0
        for x in range(1, len(A)):
            leftSum = leftSum + self.leftsum(x, A)
            rightSum = self.rightsum(x, A)
            #print leftSum, rightSum 
            #print x
            if x == 1:
                lowest = abs(leftSum - rightSum)
            if (abs(leftSum-rightSum) < lowest):
                lowest = abs(leftSum - rightSum)
            
        return lowest
    
    def leftsum(self, p, A):
        total = 0
        for p in range(p-1, p):
            total = total + abs(A[p])
        return total
    
    def rightsum(self, p, A):
        total = 0
        for p in range(p, len(A)):
            total = total + abs(A[p])
        return total
    
    def efficient(self, A):
        leftsum = A[0]
        rightsum = sum(A[x] for x in range(1, len(A)))
        min_dif = abs(leftsum - rightsum)
        for x in range(1, len(A)):
            leftsum = leftsum + A[x]
            rightsum = rightsum - A[x]
            if abs(leftsum - rightsum) < min_dif:
                min_dif = abs(leftsum - rightsum)
        return min_dif

obj = TapeEquilibrium()
A = [3, 1, 2, 4, 3]
B = [-1000, 1000]
C = [-5, -1, -2, -4, -3]

print obj.efficient(B)