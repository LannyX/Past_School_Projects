#Assignment 0402 Human Pyramid
#Dawei Wang Apr.30,2020
#YouTube Video Link: https://youtu.be/jVlak7MCqi0  
#I have not given or received any unauthorized assistance on this assignment.

def info():
    'Introduction of this program'
    print('''
    Welcome!\n
    The human pyramin is a way of stacking people vertically in a triangle. 
    It Looks like this:
        *
       * *
      * * *
     * * * *
    * * * * *
    Each person splits their weight evenly on the two people below them in 
    the pyramid. The row and column are each zero-indexed, so the person at 
    row 0, column 0 is on top of the pyramid, and person in center of bottom 
    line on the above picture is at row 4, column 2. 
    Enter the index of the people you want, with its row index and column index,
    this program will give you the total weight on one's back. Everyone in the 
    pyraimd is exactly 128 pounds.

    Enter nothing to exit this program at any time you want.
    \n''')

def askInput():
    'Ask for the threshold that user wish to set'
    global r,c
  
    try:
        # ask for valid input
        # no input will trigger termination
        r = input('Please enter the row number:')
        if r == '':
            r = c = -1
            return r,c
        c = input('Please enter the column number:')
        if  c == '':
            r = c = -1
            return r,c
        r = int(r)
        c = int(c)
        # for any input less than 0, ask again
        # if input is valid  
        if (r >= 0 and c >= 0):
            return r,c
        print('Your input must be integer and equal or bigger than 0.')
        askInput()
    # handle exceptions and ask for input again
    except ValueError:
        print ('Value cannot be converted to integer.')
        askInput()
    except TypeError:
        print ('Invalid Value, input must be integer.')
        askInput()
    return r,c

def humanPyramid(row,column):
    '''caculate the weight on given people's back with the index of row and column.
    Enter row first and then column'''
    # if row = 0, this man is on the top
    if row == 0:
        return 0
    # for the left most people
    elif column == 0 :
        return (humanPyramid(row-1,column) + 128)/2
    # for the right most people
    elif row == column :
        return (humanPyramid(row-1,column-1) + 128)/2
    # for people stand inside 
    else:
        return (humanPyramid(row-1,column-1))/2 + (humanPyramid(row-1,column))/2 + 128

def main():
    'Run this main funtion and follow the instruction to get the weight'
    # print the introduction
    info()
    # get the input
    r,c = askInput()
    # function restart control 
    while r != -1 and c != -1:

        # get the weight for certain position
        weight = humanPyramid(r,c)
        # print the result 
        print ("The total weight on row {}, column {} is {} pound(s)".format(r,c,weight))
        print ('\n-----End of The Result-----\n')

        # restart the program
        r,c = askInput()
    
    #info of service terminated
    print("\nThanks for using this program.\nService terminated")

main()
