#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 01:10:50 2019

@author: becca
"""

## Homework 2: Python - Rebecca Stein - rcs8bg ##

# %% 1. 

# Create a dictionary

English_Russian = {"Hello" : "Привет", "How are you" : "Как дела?", "Good" : "Хорошо"}

# Translate phrases from English to Russian 

def translate_Engl_to_Rus(word) :

    if word in English_Russian:
        print (English_Russian[word])
        
    else:
        print("No translation available for " + word)
        
# Test translation function 

translate_Engl_to_Rus("Hello")
translate_Engl_to_Rus("How are you")
translate_Engl_to_Rus("Good")

# %% 2. 

# Ask user for name 

Name = input("What's your name? \n")

# Ask user for two numbers and convert to floats

Num_set = [float(i) for i in input("Enter two numbers separated by a space \n").strip().split(" ")]

print ("Hi, " + Name + "! " + str(Num_set[0]) + " times " + str(Num_set[1]) + " is " + str(Num_set[0]*Num_set[1]))

# %% 3. #

## Guessing game using while statement

answer = "Watson" # Set answer

guesses_remaining = 2 # initialize guesses 

print("Here is a guessing game. You get three tries.")

# response = input()

response = input("What is the name of the computer that played on Jeopardy? \n")

while guesses_remaining > 0: # Give two additional guesses
    
    if response == answer:
    
        break

    
    else:        
        
        guesses_remaining -= 1 # count down guesses
        
        response = input("Sorry. Guess again: ")
        
        continue
 
if response != answer:  
    print("Sorry. No more guesses. The answer is " + answer + ".")
    
else:
    print("That is right!")
    

# %% 4. 
    
# Count vowels in a sentence 

counter = {"total" : 0, "a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" : 0} #initialize count of total and individual vowels

vowels = ["a", "e", "i", "o", "u"] # define set of vowels
    
string = "are you suggesting coconuts migrate" # define string

for i in string.lower(): #convert string to lower case to make counter case insensitive. iterate through characters in string. 
    
    if i in vowels:
        
        counter["total"] += 1 # count total vowels
        
        counter[i] += 1 # count individual vowels

for i in vowels:
    
    print("The number of " + i + "'s: " + str(counter[i]) + "\n")
        

#%%  5

# Count letters in words in sentence
    
sentence = "It was almost no trick at all he saw to turn vice into virtue and slander into truth impotence into abstinence arrogance into humility plunder into philanthropy thievery into honor blasphemy into wisdom brutality into patriotism and sadism into justice Anybody could do it it required no brains at all It merely required no character"

words = sentence.split(" ")

word_count = [(word, len(word)) for word in words]

word_count.sort(key = lambda tup: tup[1])

for i in word_count:
    
    print(i[0] + ": " + str(i[1]))
    
# %% 6. 
    
# Map example
    
numbers = [1, 2, 3]

def square(number):
    return number * number

numberssq = [square(number) for number in numbers]

print(numberssq)

# Filter example

numbers = range(1,11)

evennumbers = []

for number in numbers:
    
    if number % 2 == 0:
        
        evennumbers.append(number)
        
print(evennumbers)
        
# Reduce example

sum(numbers)

# %% 7. 

class Account: # Create base Account class
    
    def __init__(self, number, balance): # Constructor
        
        self.AccountNumber = number
    
        self.AccountBalance = balance
    
    def __str__(self): # To-string method
        
        return "Account Number: " + str(self.AccountNumber) + "\n" + "Account Balance: " + str(self.AccountBalance) 

Judy = Account(234234, 33333)

print(str(Judy))
    
class Checking(Account): # Create derived Checking class
    
    def __init__(self, number, balance, fee): # Constructor
        
        self.fee = fee
        
        Account.__init__(self, number, balance)
        
    def __str__(self): # To-string method
        
        return "Account Type: Checking \n" + "Account Number: " + str(self.AccountNumber) + "\n" + "Account Balance: " + str(self.AccountBalance) 
    
    def getFee(self): # Method to retrieve fee
        return self.fee
    
    def deposit (self, amount): # Method to deposit funds
        
        self.AccountBalance += amount
        
    def withdraw(self, amount): # Method to withdraw funds
        
        if amount >= self.AccountBalance + self.fee:
            
            self.AccountBalance -= (self.AccountBalance + self.fee)
            
        else:
            print("Insufficient funds!") # Message if withdrawal amount exceeds balance
        

### Test ### 
            
check1 = Checking("1234", 500, 0.50)
print(check1)
check1.withdraw(100)
print(check1)
check1.deposit(200)
print(check1)

