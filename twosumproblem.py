# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 22:33:37 2020

@author: Sakib Muhtadee
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hash_table={}
        for i in range (n):
            hash_table[nums[i]]=i
            
        for i in range (n):
            p=target-nums[i]
            if p in hash_table :
                if hash_table[p]!=i :
                    return i,hash_table[p]
                    break
        return []