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

with open(pathInA, "r") as file:
    reader = csv.reader(file, delimiter=',')
    header = next(reader)
    for line in reader:
        dataA.append(line)

print(dataA)








