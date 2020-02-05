# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:11:51 2020

@author: Sakib Muhtadee
"""
class Solution:
    hash_table={}
    def isHappy(self, n: int) -> bool:
        i=0
        total=0
        hash_table=set()
        
        while(n!=1):
            n=sum([int(i)**2 for i in str(n)])
            if n not in hash_table:
                hash_table.add(n)
            else:
                return False
        return True
