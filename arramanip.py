# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 19:17:43 2020
Array Manipulation
@author: Sakib Muhtadee

arr=['a','b','c','d']
print(arr)
#insert at the end of an array
arr.append('e')#O(1)
print(arr)
#delete from the end of an array
arr.pop()#O(1)
arr.pop()
print(arr)
#insert an element at nth place
arr.insert(0,'p')#O(n)
print(arr)
#remove an element from an array
arr.remove('a')#O(n)
print(arr)
"""
class myarray:
    length=0
    data={}
    def _init_(self,length,data):
       #super()._init_(self)
       self.length=length
       self.data=data
    def get(self,index):
       return self.data[index]
    def push(self,item):
       self.data[self.length]=item
       self.length=self.length+1
       return self.length
    def pop(self):
       last_item=self.length-1
       del(self.data[last_item])
       self.length=self.length-1
       return last_item
    def delete(self,index):
        item=self.data[index]
        self.shift(index)
    def shift(self,index):
        for i in range(index,self.length-1):
            self.data[i]=self.data[i+1]
        del(self.data[self.length-1])
        self.length=self.length-1
   
    
ara=myarray()
ara.push('hi')
ara.push('hello')
ara.push('ciao')
print(ara.data)
ara.delete(2)
print(ara.data)
