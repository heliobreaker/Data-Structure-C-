#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:16:53 2021

@author: sakibmuhtadee
"""

class solution:
    
    def __init__(self,grid):
        self.direction=0
        self.grid=grid
        
    def spiralorder(self):
        direction=self.direction
        grid=self.grid
        arr=[]
        '''total number of elements in the grid'''
        r=len(grid)
        c=len(grid[0])
        n=r*c
        '''Initializing The limits of our grid'''
        left=0
        right=c
        top=0
        bottom=r
        
        count=0
        
        while count<n:
            
            if direction==0:
                for i in range(left,right):
                    arr.append(grid[top][i])
                    
                top=top+1
                count=count+1
                direction=direction+1
                
            elif direction==1:
                for i in range (top,bottom):
                    arr.append(grid[i][right-1])
                
                right=right-1
                count=count+1
                direction=direction+1
            
            elif direction==2:
                for i in range (right-1,left-1,-1): '''Problematic Area'''
                    arr.append(grid[bottom-1][i])
                
                bottom=bottom-1
                count=count+1
                direction=direction+1
                
            else:
                for i in range (bottom-1,top-1,-1):'''Problematic Area'''
                    arr.append(grid[i][left])
                left=left+1
                count=count+1
                direction=direction+1
                
            direction=(direction%4)
           
        return arr
            
if __name__=="__main__":
    nums=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    S=solution(nums)
    print(S.spiralorder())
        