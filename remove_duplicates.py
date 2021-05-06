#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 09:52:39 2021

@author: md.sakib muhtadee
"""
class Solutions:
    def __init__(self,arr,needsorting=True):
        if (needsorting==True) :
            self.arr=sorted(arr)
        else:
            self.arr=arr

    def remove_Duplicates(self):
        arr=self.arr
        j=0
        
        for i in range (0,len(arr)):
            
            if arr[i]!=arr[i-1]:
                arr[j]=arr[i]
                j=j+1
        
        return arr[:j]
    
if __name__=="__main__":
    nums=[1,3,1,2,3,8,3,4,10,4,5,9,5,6,7]
    S=Solutions(nums)
    print(S.remove_Duplicates())