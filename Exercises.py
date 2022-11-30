#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 17:28:36 2019

Exercises to practice

@author: Rags
"""

def SortCategoryEx1(random_list: list):
    """ Sorts the items in the list in 4 different sets:  Color, Name, fruit, number"""
    color = set()  # converting to set will take out duplicate elements
    name = set()
    fruit = set()
    number = set()
    for i in random_list:
        if i[0] == "color":
            color.add(i[1])
        elif i[0] == "name":
            name.add(i[1])
        elif i[0] == "fruit":
            fruit.add(i[1])
        elif i[0] == "number":
            number.add(i[1])
        #print("This is a color")
    print('Color Set as {} elements: {} \nName set has {} elements: {}\n Fruit Set has {} elements: {}\n Number Set has {} elements: {}'.format(len(color), color, len(name), name, len(fruit), fruit, len(number), number))

def CreateRandomListFile(howlong:int = 1000):
    """Creates a random list of stuff and writes it to a file"""
    import random
    random_list = []
    names = ['Steve', 'Bob', 'David', 'Rachana', 'Zach', 'Mike', 'Josh', 'Scott', 'Jenn', 'Cathy', 'Sharon', 'Zack', 'Carol']
    colors = ["red", "blue", "orange", "yellow", "green", "light blue", "white", "black", "pink", "purple", "cyan", "magenta", "indigo", "olive"]
    fruits = ["orange","olive","strawberry","apricot","watermelon","banana","grapes","avocado","blueberries","blackberries","cherries","cranberries","figs","guava","grapefruit","lemon"]
    numbers = ["5", "26", "19", "85", "18", "20", "78", "64", "33", "1", "35", "52", "4", "75", "94", "77", "38", "34", "87", "55"]
    f = open("randomfilelist.txt", 'w')
    for i in range(howlong):
        catagory = random.randint(1,4)
        if catagory == 1:
            index_names = random.randint(0,(len(names)-1))
            f.write("name," + names[index_names] + "\n")
        elif catagory == 2:
            index_colors = random.randint(0,(len(colors)-1))
            f.write("color,"+colors[index_colors]+"\n")
        elif catagory == 3:
            index_fruits = random.randint(0,(len(fruits)-1))
            f.write("fruit,"+fruits[index_fruits]+"\n")
        elif catagory == 4:
            index_numbers = random.randint(0,(len(numbers)-1))
            f.write("number," + numbers[index_numbers]+ "\n")
    f.close()

def SortasDict(random_list: list):
    """  converts the category data into dictionary object, however the problem is if there are multiple entries with same name and different category such as name Olive, color Olive and Fruit Olive,  while creating
    the dictionary object it will overwrite the previous entry and keep only the latest olive key with the latest found category unless one is capital and another one is not"""
    D = {}
    for i in random_list:
        D[i[1]] = i[0]
    print(D)

def gen_code_file(word):
    """generate a code word file with a secretwork embedded randomly into a file of random characters at a random location"""
    import string
    import random
    from datetime import date
    max_letters = 100000
    file_contents = ''
    ran_num = random.randint(0,max_letters-1)

    for x in range(0,max_letters):
        if x == ran_num:
            file_contents = file_contents + word
        elif (x%200) == 0:
            file_contents = file_contents + '\n'
        else:
            file_contents = file_contents + random.choice(string.ascii_letters)

#    print(file_contents)
    file = open("random_letters.txt","w")
    file.write(file_contents)
    file.close()
