#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:03:58 2019

@author: becca
"""
# Exercise 1 #
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

tips = pd.read_csv("tips.csv")

fig = plt.figure()

ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

ax1.hist(tips.total_bill, bins = 10, label = "Bills", color = "Blue")
ax1.set_title("Bills")

ax2.hist(tips.tip, bins = 10, label = "Tips", color = "Red")
ax2.set_title("Tips")

ax3.scatter(tips.total_bill, tips.tip, color = "green", marker = "o")
ax3.set_yticks([5,10])
ax3.set_xticks([10,20,30,40,50])
ax3.set_title("Bill - Tip Trend")

ax4.scatter(tips.day, tips.tip, color = "orange", marker = "o")


plt.subplots_adjust(wspace = .4, hspace = .4)








