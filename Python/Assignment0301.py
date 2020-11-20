#Assignment 0301 Goldbach's Conjecture
#Dawei Wang Apr.24,2020
#YouTube Video Link: https://youtu.be/QDafjW9MNp0
#I have not given or received any unauthorized assistance on this assignment.

def info():
    'Introduction of this program'
    print('''
    Welcome!\n
    This program will allow you to test Goldbach's Conjecture.\n
    For any given threshold, it will print the first found equation that satisifed
    Goldbach's Conjecture for every even numbers starting with 4. If you see "No 
    match for" certain number, that means this number cannot be expressed as the  
    sum of two primes.(You know it will not happen in within 4 × 10^18. So please 
    contact the author if you find so. Don't take all the credit or responsibility)\n
    You may reuse this until you wish to exit\n''')

def setRange():
    'Ask for the threshold that user wish to set'
    global max
    try:
        # ask for valid input 
        max= int(input('Please enter the threshold that you want test.'))
        # for input less than 4, ask again
        if (max >= 4):
            return max
        print('Threshold must larger than 3.')
        setRange()
    # handle exceptions and ask for input again
    except ValueError:
        print ('Value cannot be converted to integer.')
        setRange()
    return max

def findPrime(max):
    'Give the list of prime numbers within the threshold minus 1 (use for further calculation)'
    #create a default list to hold primes
    prime=[];
    # an iterative loop that find s all primes
    for i in range(2, max):
        for j in range(2,i):
            # if it can be evenly divided by some number other than 1 and itself, Not prime
            # break and check the number
            if(i%j==0):
              break
        # other numbers are primes and add them into the list
        else:
            prime.append(i)
    return prime



def findFirstEquation(num,prime):
    '''This function will find the first equation that meet Goldbach's conjection and return
    '''
    # set defualt index for prime list
    i = 0
    # check the prime less than half of target number
    # prime bigger than that is meaningless since it's the same result but number position exchanged
    while (num//2 >= prime[i]):
        # difference of number to be check and no.i prime
        dif = num - prime[i]
        # if the difference also in the prime list
        if dif in prime:
            # return these two number, smaller number first
            return prime[i],dif
        # index plus one
        i += 1
    # if there's no match for this number, print this reminder
    print ('No match for {}.'.format(num))


def printResult(i,a,b):
    '''This function gives a format of the equation of Goldbach's conjecture'''
    print('{} = {} + {}'.format(i,a,b))


def testGoldbachCon():
    '''Main funtion. Follow the instruction, give the input and check the result of Goldbach's conjection'''
    # print the introduction
    info()
    # set a defalut value that controls the reuse loop
    run = True
    # reuse loop, if True, draw the plot, if False, end this program
    while (run==True):
        # get the input from the user
        max = setRange()
        # get the corresponding prime set
        prime = findPrime(max)
        # print the equation for each even number in the range 
        for i in range(4,max+1,2):
            a, b = findFirstEquation(i,prime)
            printResult(i,a,b)
        print('-----End of The Result-----')

        # Rerun the function:
        # ask if user wish to run this program again
        resp = input('Do you want to try again?(Y/N)')
        # if input is wrong, print hint and ask user to input again
        while (resp != "Y" and resp != "N"):
            print("Your input is wrong\n")
            resp = input('Do you want to try again? Enter letter Y or N, then hit enter')
        # if user wish to exit, exit the loop
        if (resp == "N" ):
            run = False

    # print termination reminder
    print("Thanks for using this program.\nService terminated")


testGoldbachCon()