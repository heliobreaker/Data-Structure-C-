#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:39:14 2020

@author: heliobreaker
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table={}
        n=len(nums)
        
        for i in range (n):
            if nums[i] in hash_table :
                hash_table[nums[i]]=hash_table[nums[i]]+1
            else:
                hash_table[nums[i]]=1
        
        for num in hash_table:
            if (hash_table[num]==1):
                return num