#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 15:13:07 2020

@author: heliobreaker
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_list={}
        n=len(nums)
        for i in range (n):
            hash_list[nums[i]]=i
        for i in range (n):
            if(nums[i] in hash_list and hash_list[nums[i]]!=i):
                return 'true'
                break
            elif(i==n):
                return 'false'
        return []
        