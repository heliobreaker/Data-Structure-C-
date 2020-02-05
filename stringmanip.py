# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 19:27:26 2020

@author: Sakib Muhtadee
"""
import time
#def reverse word(s):
def rev_word(s):
    words=s.split(" ")
    output=''
    for word in words:
        output=output+reverse(word)+' '
        
    return output    
    
def reverse(s):
    rev=''
    for c in s:
        rev=c+rev
    return rev

s=input("Enter String:")
t1=time.time()
print(rev_word(s))
t2=time.time()
print(t2-t1)