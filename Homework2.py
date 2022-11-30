"""
Created on Wed May 20 2022

@author: Jake Carter
PiE Homework 2 file 1:
Includes gen_code_file functions for homework 2
"""
def gen_code_file(secretword:str, freq:int = 1, maxlength:int = 100000):
    """
    gen_code_file(secretword:str, freq:int = 1, maxlength:int = 100000)
    Function that generates a file containing maxlength random english letters (a to z and A to Z) and places (freq) secretword(s) in the file at a random locations
    """
    import datetime
    import string
    import random
    rowSize = 250
    dt = datetime.datetime.now()
    fname = "random_letters_new_" + dt.strftime("%m%d%Y_%H%M") + ".txt"
    #fname = "rl.txt"
    timeout = 100
    j = freq
    r = set()                                                                   #set of tuples including positions and messages to write
    firstMessage = secretword + dt.strftime("%m-%d-%Y")
    message = secretword
    if maxlength < 1:
        print("Maxlength to short")
        return -1
    if freq < 0:
        print("freq needs to be positive")
        return -1
    while j >= 0:
        timeout -= 1
        if timeout == 0:
            print("Timeout (reduce frequency or increase max length)")
            break
        if j > 0:                                                               #need to add more entries
            randomPosition = random.randint(0,maxlength - len(message))
            if randomPosition % (rowSize) >= rowSize - len(message):
                #print("Position: {} Failed, wrapping" .format(randomPosition))
                continue                                                        #randomPosition would be split by newline
            for entry in r:
                if randomPosition - entry[0] > 0:                               #attempting a position after an occupied spot
                    if (randomPosition - entry[0]) < len(entry[1]):             #the difference in positions is too small to fit the occupied entry's message
                        #print("Position: {} Failed, overlap" .format(randomPosition))
                        break
                else:                                                           #attempting a position before an occupied spot
                     if (entry[0] - randomPosition) < len(message):             #the difference in position is to small to fit the new message
                         #print("Position: {} Failed, overlap" .format(randomPosition))
                         break                                                  #randomPosition overlaps the beginning of another entry
            else:
                #print("Position: {} Success" .format(randomPosition))           #successfully found unoccupied space
                j -= 1;
                r.add((randomPosition,message))                                 #set to hold the positions of the messages
                timeout = 100
        if j == 0:                                                              #done adding entries, need to add date to first entry
            s = sorted(r, key=lambda entry: entry[0])                           #sort entries by position
            if s[0][0] % rowSize >= rowSize - len(firstMessage):                #adding the date would cause a wrapping error
                j += 1
                r.remove(s[random.randint(0,len(s) - 1)])                       #randomly remove an element and try again
                #print("Position: {} Failed, wrapping" .format(s[0][0]))
            elif s[1][0] - s[0][0] < len(firstMessage):                         #no room for date
                j += 1                                                          #will try to replace second entry
                r.remove(s[1])
                #print("Position: {} Failed, overlap" .format(s[0][0]))
            else:
                j -= 1                                                          #successfully added date to first entry, can leave while loop
                s[0] = (s[0][0],firstMessage)
    #print(s)
    i = 1
    with open(fname, "w", newline = "") as f:                                   #newline = "" to remove carriage returnon newline
        while i < maxlength:                                                    #for each letter
            if i % rowSize == 0:                                                #new line every (rowSize) characters
                f.write("\n")
            else:
                f.write(random.choice(string.ascii_letters))
            i += 1
        for entry in s:
            f.seek(entry[0])                                                    #position
            f.write(entry[1])


def findWord(filename:str, word:str):
    """
    findWord(filename:str, word:str)
    Function that searches (filename) for occurances of a (word), and returns a list of integers corresponding to the location of each occurance
    """
    l = list()
    i = 0
    try:
        with open(filename, "r") as f:
            while f.read() != "":
                f.seek(i)
                if f.read(len(word)) == word:
                    l.append(i + 1)
                i += 1
        return l
    except FileNotFoundError:
        print("Error: Invalid file name")
        return -1

def dataSorter(filename:str = "answer.csv"):
    """
    dataSorter(filename:str = "answer.csv")
    Reads (filename) csv file and sorts each entry into its respective catagory column
    """
    import csv
    categoryDict = dict()                                                       #creates a dictionary to hold a lsit of entries for each catagory
    longestLength = 0
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Category"] not in categoryDict:                             #creates a set for each catagory found
                categoryDict[row["Category"]] = set()
            categoryDict[row["Category"]].add(row["Value"])                     #adds entry to respective set
        print("There are {} unique categories in this file" .format(len(categoryDict.keys())))
        for category in categoryDict:
            print("There are {0} unique entries for the {1} category" .format(len(categoryDict[category]), category))
            if len(categoryDict[category]) > longestLength:                     #finds longest length set
                longestLength = len(categoryDict[category])

    table = list()
    table.append(sorted(categoryDict.keys(), key=str.lower))                    #First entry in table is a list of each catagory
    for i in range(1, longestLength):
        table.append(list())                                                    #For each row in the csv file, a new list is created
        for category in sorted(categoryDict.keys(), key=str.lower):             #For each catagory, append the next corresponding entry
            try:
                table[i].append(sorted(categoryDict[category], key=str.lower)[i])
            except IndexError:                                                  #This exception ocurs when the rest of the column is empty
                table[i].append('')
    print(table)
    with open("sorteddata.csv", "w", newline = "") as f:
        writer = csv.writer(f)
        for i in range(0,longestLength):                                        #writes table to csv file
            writer.writerow(table[i])

def dataRecorder(filename:str, record:dict):
    """
    dataRecorder(filename:str, record:dict)
    Opens (filename) csv file and inserts (record) dictionary of format: {"Name": record["Name"], "Weight": record["Weight"], "Height": record["Height"]}
    """
    import csv
    with open(filename, "a", newline = "") as f:
        header = ["Name", "Weight", "Height"]
        writer = csv.DictWriter(f, fieldnames = header)
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow({"Name": record["Name"], "Weight": record["Weight"], "Height": record["Height"]})
