#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:33:02 2019

@author: becca


"""


## Becca Stein - rcs8bg - Homework 4 #

import unittest

from accountCheckingClasses import * 

class AccountTestCase(unittest.TestCase):
    
# test getFee when no fee was entered

    def test_get_fee_nofee(self):
        
         # Test Case 1
         
         Checking1 = Checking(1234, 500)
         
         self.assertEqual(Checking1.getFee(), 0)
        
# test getFee when fee was entered
    
        
    def test_get_fee_fee(self):
        
         # Test Case 2
         
         Checking2 = Checking(1235, 2235, 55)
         
         self.assertEqual(Checking2.getFee(), 55)
         
        
# test deposit for valid value
    

    def test_deposit(self):
        
        # Test Case 3
        
        Checking3 = Checking(1246, 44345, 64)
        
        Checking3.deposit(1000)
        
        self.assertEqual(Checking3.AccountBalance, 45345)
        
# test deposit for invalid value
        
    
    def test_deposit_negative(self):
        
        # Test Case 4
        
        Checking4 = Checking(1247, 445, 9)
        
        self.assertEqual(type(Checking4.deposit(-5)), str)
        
# test withdraw
        
    def test_withdraw(self):
        
        # Test Case 5
         
        Checking5 = Checking(1248, 800, 100)
        
        Checking5.withdraw(400)
        
        self.assertEqual(Checking5.AccountBalance, 300)
        
        
# test withdraw for insufficient funds
        
    def test_withdraw_insufficientfunds(self):
        
        # Test Case 6 
        
        Checking6 = Checking(23423, 320, 100)
        
        Checking6.withdraw(400)
        
        self.assertEqual(Checking6.AccountBalance, 320)
        

        
if __name__== '__main__':
    unittest.main()


