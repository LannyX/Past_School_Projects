#Assignment 0501 Dice and Cups
#Dawei Wang May.08,2020
#YouTube Video Link: https://youtu.be/bVpTjcaqJQg  
#I have not given or received any unauthorized assistance on this assignment.

import random

class SixSidedDie:
    'Creat a six sided die'
    def __init__(self):
        'default face value is none, to get a numberic face value, roll the die'
        self.faceValue = None

    def __repr__(self):
        'canonical string representation of SixSidedDie'
        return 'SixSidedDie({})'.format(self.faceValue)

    def __add__(self,other):
        'overloading operator + as sum of faceValue of two dies'
        return (self.faceValue + other.faceValue)

    def roll (self) :
        'roll the die and get a random face value'
        self.faceValue = random.randint(1,6)
        return self.faceValue

    def getFaceValue (self) :
        'return the face value'
        return self.faceValue

class TenSidedDie(SixSidedDie):
    'Creat a ten sided die, subclass of SixSidedDie'
    def __repr__(self):
        'canonical string representation of TenSidedDie'
        return 'TenSidedDie({})'.format(self.faceValue)

    def roll (self) :
        'roll the die and get a random face value'
        self.faceValue = random.randint(1,10)
        return self.faceValue

class TwentySidedDie(SixSidedDie):
    'Creat a twenty sided die, subclass of SixSidedDie'
    def __repr__(self):
        'canonical string representation of TwentySidedDie'
        return 'TwentySidedDie({})'.format(self.faceValue)

    def roll (self) :
        'roll the die and get a random face value'
        self.faceValue = random.randint(1,20)
        return self.faceValue

class Cup:
     '''A cup could hold several Custom quantity of different dices
     Inculding six sided die, ten sided die and twenty sided die'''
     def __init__(self,six=1,ten=1,twenty=1):
         'default cup have one of each type of die'
         # an empty list for dices
         self.cup = []
         # set up the quantity of each typr of die
         self.six = six
         self.ten = ten
         self.twenty = twenty
         # creat different dies respectively
         for i in range(self.six):
             a = SixSidedDie()
             self.cup.append(a)

         for i in range(self.ten):
             b = TenSidedDie()
             self.cup.append(b)

         for i in range(self.twenty):
             c = TwentySidedDie()
             self.cup.append(c)


     def __repr__(self):
         'canonical string representation of Cup'
         return 'Cup({})'.format((",").join(str(i) for i in self.cup))


     def roll(self):
         'roll the cup and all the dies in the cup, return the sum of face value'
         # set a default sum 
         self.sum = 0
         # roll the dice in the cup one by one and calculate the sum
         for i in range(len(self.cup)):
             self.cup[i].roll()
             self.sum += self.cup[i].getFaceValue()
         return self.sum 

     def getSum(self):
         'return the sum'
         return self.sum


a = SixSidedDie()
a.roll()
a.getFaceValue()
a

b = TenSidedDie()
b.roll()
b


cup = Cup(1,1,1)
cup
cup = Cup(3,0,0)
cup
cup = Cup()
cup
cup.roll()
cup.getSum()
cup