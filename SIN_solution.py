# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:00:51 2020

@author: nacer
"""

import os

## Global Vars

#Path of input files
PATH = "./"

#List all input file names
FILES = []
for r, d, f in os.walk(PATH):
    for file in f:
        if '.in' in file:
            FILES.append(os.path.join(file))

''' 
    Choose the files we'll work with
        0 : './a_example.in'
        1 : './b_small.in'
        2 : './c_medium.in'
        3 : './d_quite_big.in'
        4 : './e_also_big.in'
'''
for i in range(len(FILES)):
    print(i+1,"-",FILES[i])
choice = int(input("Choose a file : "))
FILE = FILES[choice-1]

def read_input(file):
    f = open(file,"r")
    text = f.read()
    lines = text.split("\n")
    
    M,P = lines[0].split(" ")
    L = lines[1].split(" ")
    for i in range(len(L)):
        L[i] = int(L[i])
    # M is max number of slices, P is number of different pizzas, L is a list of all pizza slice number
    return int(M),int(P),L