# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:23:31 2021
@author: Gonzalo
"""

class MyArray():
    
    def __init__(self):
        """Initialize the array with two attributes:
            1- the length of the array (0, as it is empty)
            2- a dictionarie, with numerical keys for the list values """
        self.length = 0
        self.data = {}
        
    def __str__(self):
        
        """With this dunder method, calling the object.__str__() will
        return the .__dict__, which is a dictionary that contains the object's 
        attributes.
        Also calling print(object) will cause the same output."""
        return str(self.__dict__)
    
    
    def get(self, index):
        
        return self.data[index]
    
    def push(self, item): # equivalent to append
        self.data[self.length] = item
        self.length += 1
        return self.length
    
    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem
    
    def delete(self, index):
        
        self.shift_items(index)
        
        del self.data[self.length-1]
        
        return None
    
    def shift_items(self,index):
        for i in range(index, self.length-1):
            
            self.data[i] = self.data[i+1]
        
        return None

arr = MyArray()
arr.push('hi')
arr.push('how')
arr.push('are')
arr.push('you')
arr.push('dude')
#arr.shift_items(2)
arr.delete(2)
    # def push(self, item):
    #     self.data[self.]

# %%    

print(newArray)
#print(newArray.get(0))
    
# %%

    
newArray = MyArray()
try:
    print(newArray.get(0))     
except IndexError as err:
    print(err)
    

# %%
