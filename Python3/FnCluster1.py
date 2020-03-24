import os
import csv
import random
import pandas as pd


# making paths, files, and dirs using os.path.join

# var name = os.path.join("path bits in quotes broken up by ','")
# paths can be for wherever you want the thing to end up
# in the final part of the path, you need to add the file type (.txt, .csv, .pdf etc...)

pathOutA = os.path.join("TestReso", "Output", "outputA.txt")

pathInA = os.path.join("TestReso", "Input", "inputA.csv")

# Reading in csv's using the 'with' operator
# it makes your life easier by saving the data to a varible when you read it in so its easier to access when you need it

dataA = []
# with open(path, what you want to do) as "Temp var name"
with open(pathInA, "r") as file:
    # setting the reader as a variable saves time
    # the Delimiter is what the values are separated by in the csv. default is the ,
    reader = csv.reader(file, delimiter=',')
    # Header saves the first line with the key for how the info is saved. not all csv's have a header
    # next(reader) is what actually saves the first line
    header = next(reader)
    # loop through the file and save the data into our local var
    # this saves us from having to re-read it every time we want to look at the data or do anything with it
    for line in reader:
        dataA.append(line)
print(dataA)
print("\n\n\n")

# Generate some random data we can save in a csv
# list Comprehension
#              output          loop-iner  iterator   loop-outer
dataB = [[random.randint(0, 100) for j in range(5)] for i in range(10)]
for line in dataB:
    print(line)

# Checks if path is valid. if it is, it creates a txt file containing the data
# else it gives as os error
try:
    #           path    w+ is write or create if not there
    #                            newline="" removes the blank line in-between lines
    with open(pathOutA, "w+", newline="") as dataOut:
        writer = csv.writer(dataOut, delimiter='\t')
        for row in dataB:
            writer.writerow(row)
except OSError:
    print("Creation of txt file failed")
else:
    pass







