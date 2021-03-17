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
        
    
    def __str__(self):
        return "MyClass(wheels" + " " +  str(self.wheels)
    
    @classmethod
    def info(cls):
        if cls.start == True:
            status = "Start"
        else:
            status = "Stop"
        
        return print(f"this movil status is: {status}")


Movil.info()  # calling a class method

car = Movil(wheels=4, gates=3) # instanciate a movil object

# %%

# Here all three give the same output, which is the pointer of our object. 
# When __str__, print(), or str() are called you will get your defined output
#. Make note that the __repr__ output remains the same.

print(car.__str__())
print(car.__repr__())
print(car)


# %%
print(dir(Movil))
print(dir(car)) # same but also wheels and gates.
# %%
print(type(car))


# %%
print(newArray.__delattr__())

print(newArray.__class__())