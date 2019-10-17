#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:50:58 2019

@author: becca

Binary Search Algorithm Implementation
"""

def binarySearch(ordered_list, target):
        """ Returns -1 if value is not in list, otherwise returns index of value """   
        upper = len(ordered_list) - 1
        
        lower = 0
        
        while upper >= lower:
        
            mid = (upper + lower) // 2
        
            if ordered_list[mid] == target:
            
                return mid
                
            elif ordered_list[mid] < target:
                
                lower = mid + 1
                
            else:
                
                upper = mid -1
                
        return -1


