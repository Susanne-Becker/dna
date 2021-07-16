###
#-------------------------------------------------------------------------------
# dna.py
#-------------------------------------------------------------------------------
#
# program that identifies a person based on their DNA
#
# Gemaakt door: Susanne Becker
#
###

import csv
import sys

def main():
    # read database
    with open(sys.argv[1], 'r') as database:
        datalist = csv.reader(database)
        data = [row for row in datalist]

    # read sequence data
    with open(sys.argv[2], 'r') as sequences:
        dna = sequences.read()

    # list to store counter
    counter = []

     # loop through all STR, count how many times STR repeats
     # range(1, len(data[0])) means 'range(start, stop)'
    for j in range(1, len(data[0])):
        number = 1
        while data[0][j] in dna:
            number += 1
        counter.append(str(number - 1))

    # loop through all rows in database, compare STR count with every row
    for k in range(1, len(data)):
        if data[k][1:len(data[0])] == counter:
            print(data[k][0])
            sys.exit()
    print('No Match')
    
    

if __name__ == "__main__":
    main()