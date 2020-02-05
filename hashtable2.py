#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 12:01:12 2020

@author: heliobreaker

"""
class hashtable():
    def __init__(self, length=4):
        self.array = [None] * length

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        
        index = self.hash(key)
        if self.array[index] is not None:
            
            for kvp in self.array[index]:
               
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
        
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            raise KeyError()
    
ara=hashtable(5)
ara.add('sakib',1)
ara.add('sazia',2)
ara.add('sifat',3)
ara.add('nipu',4)
