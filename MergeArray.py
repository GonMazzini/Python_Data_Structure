# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:50:52 2021

@author: Gonzalo
"""

arr1 = [0,3,4,31]
arr2 = [4,6,30]

# %%
def mergedSortedArrays(arr1,arr2):
    arr1.extend(arr2)
    arr1.sort()
    return arr1
#arr1.extend(arr2).sort()
    
    
    



mergedSortedArrays([0,3,4,31], [4,6,30])
 # [0,3,4,4,6,30,31]    
    
 
