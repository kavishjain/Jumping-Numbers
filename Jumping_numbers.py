# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 14:47:20 2020

@author: jnk5kor
"""
#program to print the jumping numbers :- whose adjacent no. digits difference is 1 or -1
x=int(input("Print any positive number"))
for num in range(10,x):
    a=str(num)
    for i in range(0,len(a)-1):
        diff=int(a[i])-int(a[i+1])
        if abs(diff)==1:
            if i==len(a)-2:
                print(a)
        else:
            break



