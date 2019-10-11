#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:56:49 2019

@author: becca
"""

# Rebecca Stein - rcs8bg - In-Class Assignment 7-11-2019 #

# Example of map function use: Batching a process across multiple files #

import re 
import os

os.chdir("/Users/becca/Documents/MSDS/Programming/Some text files")

def word_count(file_path):
    
    count = 0 # init word count
   
    in_File = open(file_path, 'r') # open file in read mode
    
    contents = in_File.read()
    
    contents_clean = re.split('\s', contents) # split file into words
    
    for word in contents_clean: # count words in file
        
        count += 1 # init count
                    
    print(file_path + " word count: " + str(count)) # print result
    
    
    in_File.close()

list(map(word_count, ["sample.txt", "sample2.txt", "sample3.txt"]))


