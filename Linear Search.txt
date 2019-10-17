#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:18:13 2019

@author: becca
"""

# Linear Search Algorithm Example #

def linearSearch(target, my_list): # Search list for target value
    
    for i in my_list: # Iterate through list until first instance of target value is found
        
        if i == target:
            
            return my_list.index(i)
        
    if target not in my_list: # Return message if target is not in list
        
        return "Target not found"
    

fruit = ["pear", "apple", "grape", "banana", "mango", "apple"]


print(linearSearch("apple", fruit))

print(linearSearch("carrot", fruit))

print(linearSearch("grape", fruit))

print(len(fruit))
     
