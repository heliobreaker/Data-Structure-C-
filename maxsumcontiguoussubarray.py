#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 20:07:49 2021

@author: heliobreaker
"""

class Solutions:
    def __init__(self,arr):
        self.arr=arr 

    def maxsum(self):
        arr=self.arr
        currentSum=0
        maxSum=-9999999999999
        
        for i in range (0,len(arr)):
            currentSum=currentSum+arr[i]
            if currentSum>maxSum:
                maxSum=currentSum
            if currentSum<0:
                currentSum=0
                
        return maxSum
    
if __name__=="__main__":
    nums=[-1,-2,-10,-5,-4,50]
    S=Solutions(nums)
    print(S.maxsum())