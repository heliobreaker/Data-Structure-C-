# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 21:19:02 2020

@author: Sakib Muhtadee
"""

a1=[1,2,3,7,9]
a2=[2,3,4,5]

def mergesortedarray(a1,a2):
    n1=len(a1)
    n2=len(a2)
    m=n1+n2
    mer_ara=[]
    if(n1==0):
        return a2
    elif(n2==0):
        return a1
    i1=0
    i2=0
    for i in range (m):
        if(i1<n1 and i2<n2):
            if(a1[i1]<a2[i2]):
                mer_ara.append(a1[i1])
                i1=i1+1
            else:
                mer_ara.append(a2[i2])
                i2=i2+1
        elif(i1==n1):
            while(i2<n2):
                mer_ara.append(a2[i2])
                i2=i2+1
        elif(i2==n2):
            while(i1<n1):
                mer_ara.append(a1[i1])
                i1=i1+1
    
    return mer_ara
print(mergesortedarray(a1,a2))
    