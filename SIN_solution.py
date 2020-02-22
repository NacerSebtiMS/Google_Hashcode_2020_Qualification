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
        if '.txt' in file and "solution" not in file:
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
    BL = list( map(int, lines[1].split(" ")))
    LL= []
    for i in range(int(L)):
        LL +=  [ list(map(int,lines[2*i+2].split(" "))) + [ list(map(int,lines[2*i+3].split(" "))) ] ]
    return int(B),int(L),int(D), BL, LL

B,L,D,BL,LL = read_input(FILE)

def scorify_library(library):
    """
    The aim is to give the libraries a score, that will enable to order them later on
    """
    NB = library[0]
    BD = library[2]
    SB = library_total_book_score(library)
    DR = library[1]
    library_scoring = (D - DR) * BD * (SB/NB)
    return library_scoring



def library_total_book_score(library):
    book_ids = library[3]
    total_library_book_score = 0
    for id in book_ids:
        total_library_book_score += BL[id]
    return total_library_book_score


# Scores --> list of tuple (id lib, score)
scores = []
for i in range(len(LL)):
    scores += [( i, scorify_library(LL[i]) ) ]
scores.sort(key=lambda tup: tup[1])

def compute_available_days():
    available_libraries = []
    availability_day = 0
    while len(scores)>0:
        library_id_score = scores.pop()
        library_id = library_id_score[0]
        DR = LL[library_id][1]
        availability_day += DR
        if availability_day > D:
            continue
        else:
            entry = (library_id,availability_day)
            available_libraries.append(entry)
    return available_libraries

AvL = compute_available_days() # Availability of libraries following the scoring

def available_libs(d):
    AvLD = []
    day = AvL[0][1]
    i = 0
    ln = len(AvL)
    while i<ln and day <= d:
        AvLD += [AvL[i]]
        day = AvL[i][1]
        i+=1
    return AvLD

ScB = [] #Scanned books
ScBpL = [] #Scanned books per lib
LL2 = LL.copy()

for d in range(D):
    print("Day %d/%d\t\t%.2f%%" % (d,D,d/D*100))
    AvLD = available_libs(d)
    for lib in AvLD:
        id_lib = lib[0]
        scan_rate = LL2[ id_lib ][2]
        
        for book in LL2[id_lib][3]:
            if scan_rate == 0:
                continue
            
            if book in ScB:
                LL2[id_lib][3].remove(book)
            else :
                ScBpL += [ (book,id_lib) ]
                ScB += [book]
                scan_rate -= 1
                
LIBS = available_libs(D)
nbr_libraries_for_sign_up = len(LIBS)
libraries_submission = [ [] ]*nbr_libraries_for_sign_up


library_dict = {}
temp_lib = 0

for book in ScBpL:
    if book[1] not in library_dict.keys():    
        library_dict[book[1]]=[]
    library_dict[book[1]].append(book[0])

OUT = "Solutions/" + FILE[:-4] + "_solution.txt"

f = open(OUT,"w+")
f.write(str(nbr_libraries_for_sign_up))
f.write("\n")
for lib in LIBS:
    BOOKS = library_dict[lib[0]]
    f.write(str(lib[0]))
    f.write(" ")
    f.write(str(len(BOOKS)))
    f.write("\n")
    for b in BOOKS:
        f.write(str(b))
        f.write(" ")
    f.write("\n")
f.close()