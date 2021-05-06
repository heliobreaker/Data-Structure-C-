#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 12:25:44 2021

@author: md.sakib muhtadee
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for i in range (0,len(nums)):
            if nums[i]!=val:
                nums[j]=nums[i]
                j=j+1
        return j
