#Assignment 0401 Goldbach's Deuce
#Dawei Wang Apr.30,2020
#YouTube Video Link: https://youtu.be/fWPXhHtdqqY 
#I have not given or received any unauthorized assistance on this assignment.

import random

def info():
    'Introduction of this program'
    print('''
    Welcome!\n
    This program will allow you to test Goldbach Deuce
    Enter the number of random numbers you wish to create
    Then enter a number that you want to test whether if there's sum of two 
    numbers in this newly created random numbers list that equal to this number

    Exit any time by entering nothing.
    \n''')

def askInput():
    'Ask for the threshold that user wish to set'
    global i,n
    try:
        # ask for valid input if input is none, return -1 for a termination 
        i = input('Please enter the number of random numbers you want to generate.')
        if i == '':
            i = n = -1
            return i,n
        n = input('Please enter the number that you want test.')
        if n == '':
            i = n = -1
            return i,n
        i = int(i)
        n = int(n)
        # for any input less than 0, ask again
        if (i >= 0 and n >= 0):
            return i,n
        print('Your input must be integer and equal or bigger than 0.')
        askInput()
    # handle exceptions and ask for input again
    except ValueError:
        print ('Value cannot be converted to integer.')
        askInput()
    except TypeError:
        print ('Invalid Value, input must be integer.')
        askInput()
    return i,n

def getRandom (n):
    'generate a list with n random number'
    # create a empty list
    list = []
    # create random number and put it in the list
    for i in range(n):
        list.append(random.randint(0,100))
    # sort the list
    list.sort()
    return list

def recBinSearch(x,nums,low,high):
    'give the target number x and the list, conduct the binary search of list nums'
    # This is a function that taught in the class
    # no place left to look
    if low > high:
        return -1
    mid = (low+high)//2
    item = nums[mid]
    if item == x:
        return mid
    # look in lower half
    elif x < item:
        return recBinSearch(x, nums,low,mid-1)
    # look in upper half
    else:
        return recBinSearch(x,nums, mid+1, high)

def search(x, nums):
    'conduct the binary search'
    return recBinSearch(x, nums, 0,len(nums)-1)

def testGoldbachDeuce(n,nums):
    "for n, test if there's a pair of number in the list can be sum to n"
    # set default i
    i = 0
    # no need to test second half
    while n//2 >= nums[i]:
        # calculate the difference between n and element in the list
        dif = n - nums[i]
        # binary search and see whether the difference in the list 
        res = search(dif, nums)
        # if return value of search isn't -1, the difference in the list
        # return these two numbers in the list
        if res != -1:
            return nums[i],dif
        i += 1
    # if there's no match, return -1 as indicator 
    return -1,-1


def printResult(i,a,b):
    '''This function gives a format of the equation of Goldbach deuce'''
    print('{} = {} + {}'.format(i,a,b))

def main():
    'Run this function, follow the instruction and test for the Goldbach deuce'
    # print the introduction 
    info()
    # get the input parameter
    i,n = askInput()
    # function restart control
    while i != -1 and n != -1:
        # set the random list
        nums = getRandom(i)
        # test for the Goldbach deuce
        res,dif = testGoldbachDeuce(n,nums)
        # if it has match print the result 
        if res != -1:
            printResult(n,res,dif)
        # if there's no match, print the none result 
        else: print("There's no match, check the result below")
        # print the request number and random list for checking
        print ("Your number is {}, and the list of random are:".format(n))
        print (nums)
        print ('\n-----End of The Result-----\n')

        # restart the program
        i,n = askInput()
    
    #info of service terminated
    print("\nThanks for using this program.\nService terminated")
    
main()