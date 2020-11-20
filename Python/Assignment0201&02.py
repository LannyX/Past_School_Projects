#Assignment 0202 Stem-and-Leaf Implementation
#Dawei Wang Apr.19,2020
#YouTube Video Link:https://youtu.be/NlVMkFnVccE 
#I have not given or received any unauthorized assistance on this assignment.

import collections
import sys

def info():
    'This is an introduction'
    print("\nThis application will give allow you to choose different datafiles and convert them into a stem and leaf plot\n")


def fileSelect():
    'Ask user select pre-set datafile and return this input number'
    # ask the user to select datafile index number
    num= int(input('Please select datafile 1 2 or 3. Type the number and hit enter.'))
    return num


def fileConvert(n):
     'This function will convert datafile selected by user into a list contains all the numbers in the file  \
     \n Input parameter is datafile index. A list will return'
     # Define file name and pass the corresponding file path to the filename
     # This part could be substituted by other paths
     if (n==1):
         #r before string convert string to raw string and make it readable as a path
         filename = r"C:\Users\rocke\iCloudDrive\Desktop\Python Projects\Assignment0201\StemAndLeaf1.txt"
     elif (n == 2):
         filename = r"C:\Users\rocke\iCloudDrive\Desktop\Python Projects\Assignment0201\StemAndLeaf2.txt"
     elif (n == 3):  
         filename = r"C:\Users\rocke\iCloudDrive\Desktop\Python Projects\Assignment0201\StemAndLeaf3.txt"
     # Open the datafile with file name, read file and save it in to lineList, then close the file
     infile = open(filename,"r")
     lineList = infile.readlines()
     infile.close()
     #set a new empty list named value 
     value = []         
     # add data in data file one by one to the list named value
     # chop any possible symbol and only keep the number
     for i in range(0,len(lineList)):
         value.append(int(lineList[i].strip()))
     # return the list after converting all data into this list
     return value 


def getLeaf(values):
    'The dictionary contains corresponding lists that could store leaves \
    \nInput a list this function will find the leaf value for each element and store it in a list with index that \
    is its stem number'
    # create a dictionary for the storage later
    leaves = collections.defaultdict(list)
    # set defalut min stem and max stem for furture opeartions
    min = max = values[0] // 10
    # calculate each element in the input list and put them into corresponding list in the dictionary 
    for v in values:
        # get one digit leaf and no limitations on stem
        leaves[v//10].append(v%10)
        # a is corresponding stem  
        a = v//10
        # check the min and max and reset them if necessary
        if min > a:
            min = a
        if max < a:
            max = a
    # return leaves dictionary and min and max of stem
    return leaves, min, max


def setStem(sMin, sMax):
    'Construct a list of stem by using input min and max value'
    # set the stem list for the datafile. It contains all stem number from the minimum to maximum  
    stem = list(range(sMin,sMax+1))
    # return the stem list
    return stem


def setStemAndLeaf(num):
    'This function allows us return the stem and leaves container. Input the datafile index, it will return stem and leaves'
    # call fileConvert function
    value = fileConvert(num)
    # pass the value and call getLeaf function
    leaves, min, max = getLeaf(value)
    # pass min and max and call setStem function
    stem = setStem(min, max)
    # return converted stem and leaves
    return stem,leaves


def printStemLeaf(Stem,Leaves):
    'This function print the results in preset format. Input stem and leaves, it will draw the plot for you.'
    # print the head of plot
    print("The Stem-and-Leaf Plot")
    # traversal containers and print the result 
    for i in range(0,len(Stem)):
        # x is stem 
        x = str(Stem[i])
        #sort the Leaves
        Leaves[Stem[i]].sort()
        #convert Leaves in to a string with space in between and store it in y 
        y = " ".join(map(str,Leaves[Stem[i]]))
        #print No.i+1 row with stem x and leaves y
        print(x +"\t| " + y)

 
def main():
    'Follow the instruction, give your choice and print the stem and leaf plot'
    print ("Welcome!")
    # print the introduction
    info()
    # set a defalut value that controls the reuse loop
    run = True
    # reuse loop, if True, draw the plot, if False, end this program
    while (run==True):
        # call fileSelect function
        num = fileSelect()
        # if input is wrong, print hint and ask user to input again
        while (num != 1 and num != 2 and num != 3):
            print("Your input is wrong")
            num = fileSelect()
        # call setStemAndLeaf and generate stem and leaves
        Stem,Leaves = setStemAndLeaf(num)
        # call printStemLeaf and draw the plot
        printStemLeaf(Stem,Leaves)
        # ask if user wish to run this program again
        resp = input('Do you want to try again?(Y/N)')
        # if input is wrong, print hint and ask user to input again
        while (resp != "Y" and resp != "N"):
            print("Your input is wrong")
            resp = input('Do you want to try again? Enter letter Y or N, then hit enter')
        # if user wish to exit, exit the loop
        if (resp == "N" ):
            run = False
    # print termination reminder
    print("Thanks for using this program.\nService terminated")


main()