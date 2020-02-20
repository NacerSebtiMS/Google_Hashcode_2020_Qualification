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
        if '.txt' in file:
            FILES.append(os.path.join(file))

''' 
    Choose the files we'll work with
        1 - a_example.txt
        2 - b_read_on.txt
        3 - c_incunabula.txt
        4 - d_tough_choices.txt
        5 - e_so_many_books.txt
        6 - f_libraries_of_the_world.txt
'''
for i in range(len(FILES)):
    print(i+1,"-",FILES[i])
choice = int(input("Choose a file : "))
FILE = FILES[choice-1]

def read_input(file):
    f = open(file,"r")
    text = f.read()
    lines = text.split("\n")
    
    B,L,D = lines[0].split(" ")
    BL = lines[1].split(" ")
    LL= []
    for i in range(int(L)):
        LL +=  [ lines[2*i+2].split(" ") + [lines[2*i+3].split(" ")] ]
    return int(B),int(L),int(D), BL, LL

B,L,D,BL,LL = read_input(FILE)