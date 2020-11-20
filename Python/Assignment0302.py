#Assignment 0301 Happy Primes
#Dawei Wang Apr.24,2020
#YouTube Video Link: https://youtu.be/fG-h_1KmrhM 
#I have not given or received any unauthorized assistance on this assignment.

def info():
    'Introduction of this program'
    print('''
    Welcome!\n
    This program will allow you to test wheather if a positive integer is a happy number 
    or sad number, as well as prime or non-prime.
    Follow the instructions and give the input, you will see the result. After input the
    number, hit enter to check the result. Input nothing and hit enter to exit any time 
    you want.\n''')

def askInput():
    'Ask for the input from user'
    global numb
    try:
        #ask for the input
        numb= input('Please enter a positive integer that you want to test.')
        #return -1 as indicator for ending this program if nothing input
        if numb == '':
           numb = -1
           return numb
        #ask for the correct format input
        numb = int(numb)
        if (numb > 0):
            return numb
        print('The number must be positive.')
        askInput()
    except ValueError:
        print ('Value cannot be converted to integer.')
        askInput()
    except TypeError:
        print ('Invalid Value, input must be integer.')
        askInput()
    return numb

def isHappy(n):
    'This function will give a verdict on whether the input is happy number or not'
    #creat an empty set A set could store none-repetitive numbers
    inter = set()
    #set a temporary number that could caluate sum of squares of it's digit 
    temp = n

    while True:
        # caluate sum of squares of it's digit and replace last temp 
        temp = sum (temp)
        # if the sum = 1 at certain point, it is a happy number, return true
        if temp == 1 :
            return True
        # if the new temp in the inter set, it will get in to a endless loop
        # it is a sad number, return false
        if temp in inter:
            return False
        # for a temp that is never showed up in inter before, add it to the set
        inter.add(temp)

def sum(n):
    'This function will give the sum of the squares of its digits'
    # set a default value
    sqsum = 0
    # calculate the sum of squares of its digits iteratively
    while n/10 > 0:
        sqsum += (n%10) * (n%10)
        n = n//10
    return sqsum

def isPrime(num): 
    'This function will give a verdict on whether the input is prime'
    # prime cannot be less or equal to 1
    if num <= 1:    
        return False
    # 2 is the only even prime 
    if num == 2: return True
    # even number above 2 isn't prime 
    if num % 2 == 0: return False 
    # set default i
    i = 3   
    # find if there's a number can be devided evenly with the range of [3, its square root]
    while i**2 <= num:    
        if num % i == 0:    
            return False   
        i += 1 
    # if there's this number it's a prime    
    return True  

def main():
    'Main funtion. Follow the instruction, give the input and check the result of the number. It will determine if its happy number or prime'
    #print introduction
    info()
    #ask for the input from user
    n = askInput()

    while n != -1:
        
        #Give a verdict of the input number
        #Both True for Happy Prime
        if isHappy(n) == isPrime(n) == True:
            print("\n{} is a Happy prime".format(n))
        #Both False for Sad Non-prime
        elif isHappy(n) == isPrime(n) == False:
            print("\n{} is a Sad non-prime".format(n) )
        #Is happy but not prime: Happy Non-prime
        elif isHappy(n) == True and isPrime(n) == False:
            print("\n{} is a Happy non-prime".format(n))
        #The only possiblity left is Sad Prime
        else : print("\n{} is a Sad prime".format(n))
        print('\n-----End of The Result-----\n')
        n = askInput()

    #info of service terminated
    print("\nThanks for using this program.\nService terminated")
  
main()