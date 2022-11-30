"""
Created on Wed May 24 2022

@author: Jake Carter
PiE Homework 2 file 2:
Code for creating a record of height and weight data in a csv file
Uses dataRecorder function from Homework2 file
"""
import sys
import re
try:
    name = str(input('Enter name: '))
    if re.compile("[@_!#$%^&*()<>?/\|}{~:]").search(name) != None:
        print('Invalid entry')
        sys.exit(-1)
    weightlbs = float(input('Enter weight (lbs): '))
    heightft = float(input('Enter height (ft): '))
except ValueError: # catches any non number inputs
    print('Invalid entry')
    sys.exit(-1)

record = {"Name":name , "Weight":weightlbs, "Height":heightft}
import Homework2
Homework2.dataRecorder("Data.csv", record)

sys.exit()
