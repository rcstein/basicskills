#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:50:58 2019

@author: becca
"""



# Classwork 5 (part 2) - Rebecca Stein - rcs8bg

# Binary Search Algorithm Example #

# class version #

#class orderedList:
    
    #def __init__(self, ordered_list):
        
#        self.ordered_list = ordered_list
#
#    def binarySearch(self, target):
#    
#        midpoint = int(len(self.ordered_list) / 2)
#    
#        pos = midpoint
#    
#        searched = [midpoint]
#    
#        while 0 <= pos <= (len(self.ordered_list) - 1):
#        
#    
#            if self.ordered_list[pos] == target:
#                
#                print("Positions searched:" + str(searched))
#            
#                return self.ordered_list.index(target)
#        
#            elif self.ordered_list[pos] < target:
#            
#                pos +=1
#                
#                searched.append(pos)
#            
#            else:
#            
#                pos -= 1
#                
#                searched.append(pos)
#            
#        print("Positions searched:" + str(searched))
#        
#        return "Target not found"
    
    
    
# function version # 

def binarySearch(ordered_list, target):
    
        midpoint = int(len(ordered_list) / 2)
    
        pos = midpoint
    
        searched = [midpoint]
    
        while 0 <= pos <= (len(ordered_list) - 1):
        
    
            if ordered_list[pos] == target:
                
                print("Positions searched:" + str(searched))
            
                return ordered_list.index(target)
        
            elif ordered_list[pos] < target:
            
                pos +=1
                
                searched.append(pos)
            
            else:
            
                pos -= 1
                
                searched.append(pos)
            
        print("Positions searched:" + str(searched))
        
        return "Target not found"
    


#print(binarySearch([-1, 4, 5, 11, 13], 4))

print(binarySearch([-1, 4, 5, 11, 13], 9))

#print(binarySearch([-5, -2, -1, 4, 5, 11, 13, 14, 17, 18], 3))



