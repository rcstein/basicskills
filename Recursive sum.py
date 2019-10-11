#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:53:21 2019

@author: becca
"""

# list sum with recursion #

def sum_two(listex):

    
    if len(listex) == 1:
    
        return listex[0]
    
    else:
        
        return listex[0] + sum_two(listex[1:])

    

print(sum_two([3, 4, 5, 6, 7, 1]))