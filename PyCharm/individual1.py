#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    num = int(input("Vvedite chislo"))
    if num <= 0 and num >= 12:
        print() 
    days = 0
    polyg = 0
    if num in [4, 6, 9, 11]:
        days = 30
    elif num == 2:
        days = 28
    else:
        days = 31

    if num <= 6:
        polyg = 1
    else:
        polyg = 2
    print(f"polygodie = {polyg}\nkol-vo dney = {days}")
