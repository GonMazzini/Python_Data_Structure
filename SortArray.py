# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:16:21 2021

@author: Gonzalo
"""

""" Create a function that reverses a string:
    
    'Hi My Name is Gonzalo'
    'aloznoG si emaN yM iH"""
    
def reverse(string):
    
    backwards = []
#    totalItems = len(str) - 1
    
    for i in range(1, len(string) +1):
    
        #print(len(string) - i)
        backwards.append(string[len(string)-i])
       # print(backwards)
        
        
   # print("".join(map(str, backwards)))
    output = "".join(map(str, backwards))
        
    return print(output)

def reverse2(string):
    
    output = "".join(reversed(string))
    
    return print(output)


reverse("Hi My Name is Gonzalo")
reverse2("Hi My Name is Gonzalo")


#%%
for i in range(10,1):
    print(i)