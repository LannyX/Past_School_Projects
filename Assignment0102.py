#Assignment 0102 Coprime
#Dawei Wang Apr.9,2020
#YouTube Video Link: https://youtu.be/Hvp7sS8yxuo
#I have not given or received any unauthorized assistance on this assignment.

def coprimeTestLoop():
    'This function allows you to check whether two numbers are coprime \
    \nInput two numbers following instruction successively and you will find the answer\n'
    
    #Print instruction 
    print('Please enter two positive integers that you wish to check successively. \
    \nRestart the function if crash\n')
    
    #Set two varibles a and b to store the input and pass to the coprime function
    a = eval(input('Please type the First number below and then hit Enter:'))
    b = eval(input('Please type the Second number below and then hit Enter:'))
    
    #Print conclusion based on the return value of coprime function 
    if (coprime(a,b)==True):
        print("They are coprimes.")
    else:
        print("They are not coprimes.")

    #Ask for another comparision 
    ip = input('Would you like to compare another pair?(Y/N)')
    if (ip == 'Y' ):
        coprimeTestLoop()
    else:
        print('Thanks for using this function.')


def coprime(a,b):
    'This function if two input parameters are coprime, put numbers to ckeck as this format \
    \ncoprime(3,7) or coprime(18,24)\nThe return value will be boolean. True means coprime'
    
    #recursive way of division algorithm 
    #recognize the bigger number to set dividend and divisor 
    if (a > b):
        #set base case:a and b can be divided evenly 
        if (a%b == 0):
            if (b == 1):
                return True
            return False
        return coprime(b, a%b)

    #if a<=b set b as dividend
    #base case: b and a can be divided evenly
    if (b%a == 0):
        if(a == 1):
            return True
        return False
    return coprime(a, b%a)

coprimeTestLoop()
                                                   