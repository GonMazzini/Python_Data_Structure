# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 17:40:06 2021

@author: Gonzalo
"""
# Dunder methods


class Movil():
    
    start = False
    stop = True
    
    def __init__(self, wheels, gates):
        self.wheels = wheels
        self.gates = gates
        
    def info(cls):
        if start == True:
            status = "Start"
        else:
            status = "Stop"
        
        return print(f"this movil status is {status}")
        
        



# %%
print(newArray.__delattr__())

print(newArray.__class__())