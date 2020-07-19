# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 19:49:47 2020

@author: MADCAT
"""

while True:
    x = int(input("Pls enter a year: "))
    if (x % 400 == 0) or (x % 4 == 0 and x % 100 != 0):
        print(f"{x} is a leap year")
        break
    else:
        print(f"{x} is not a leap year")
        break