#Assignment 0101 Grading Logic
#Dawei Wang Apr.8,2020
#YouTube Video Link: https://youtu.be/DKA5CYK1EAo
#I have not given or received any unauthorized assistance on this assignment.

def grad():
    'Follow the instructions and input corresponding answer, this function will grade the assignment \
    \nEnter the answer of each question and you will see the final score'
    #set the default score
    score = 0.0
    #set the default penalty rate
    penaltyRate = 0
    
    #Reminder of correct input format
    print("Please enter captial letter Y or N for following Questions \
    \nOther inputs may cause failuer or erroneous results:\n")

    #critical is used to determine if this assignment fail to follow critical requirment 
    critical = input('Is the assignment summitted as a single uncompressed.py file?(Y/N)')
    #if it's fail to follow critical requirment, then return default score which is 0
    if critical == "N":
        print("The Final Score is:")
        return score

    critical = input("Are there authors' name amd date in the assignment ?(Y/N)")
    if critical == "N":
        print("The Final Score is:")
        return score

    critical = input('Is honor statement inculded in the assignment?(Y/N)')
    if critical == "N":
        print("The Final Score is:")
        return score

    critical = input('Is unlisted YouTube Video link provided in the assignment?(Y/N)')
    if critical == "N":
        print("The Final Score is:")
        return score

    #Ask for late submission 
    if input('Was the assignment submitted on time?(Y/N)') != 'Y':
        #Set penalty rate, for every hour late, deduct 0.4 from the orginal grading
        penaltyRate = 0.4*eval(input('How many hours late?(Enter positive integer)'))

    #Reminder of correct input format
    print("Evaluate the followings with the scale of 0 to 10,please enter numbers here \
    \nDecimals are supported\n")

    #Ask grade of each criteria and add them to score
    score += eval(input('How well the correctness of the code?(0-10)'))
    score += eval(input('How well the elegance of the code?(0-10) \
    \n(data structure selection, algorithm efficiency, function implementation, etc.)'))
    score += eval(input('Code hypiene (white space, docstrings, etc.) evaluation (0-10)'))
    score += eval(input('Discussion quality in YouTube video (0-10)'))

    #Calculate final score after deducting penalty 
    score -= penaltyRate
    
    #For submissions that is too late to have a postive score, set score to 0
    if score < 0:
        score = 0
    print("The Final Score is:")
    return score


grad()

