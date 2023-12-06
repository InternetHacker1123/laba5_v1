#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    for i in range(100, 1000):
        i = str(i)
        sum = int(i[0]) + int(i[1]) + int(i[2])
        if sum % 7 == 0 and int(i) % 7 == 0:
            print(i)
        else: 
            continue 