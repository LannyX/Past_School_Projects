#Assignment 0601 Palindrome Dates
#Dawei Wang May.12,2020
#YouTube Video Link: https://youtu.be/050Go0L8OZU
#I have not given or received any unauthorized assistance on this assignment.

class Date:
    '''The Date class provides getDates function that allow you to find the palindrome dates in the range of 
    year you assign'''
    def getDate(self,start,end):
        '''This function will allow you enter a start year and a end year. It will print the palindrome dates
        in between this range (inculding the start and end year) DD/MM/YYYY format'''
        # transfer start and end year in int format 
        start =int(start)
        end = int(end)
        # open a output file
        outfile = open(r'D:\\Output\\Palindrome.txt','w')
        # print the header
        outfile.write('Palindrome Dates between {} and {} are followings:\n(DD/MM/YYYY)\n'.format(start,end))        
        # for each year reverse the string and chech if its a valid date
        for year in range (start,end+1,1):
            # transfer year to string
            years = str(year)
            # reverse the year and save it in rev
            rev = years[::-1]
            # chech if its valid if True write the result in output file
            if self.validDay(rev) :     
                outfile.write('{}/{}/{}\n'.format(rev[:2],rev[2:4],year))


    def validDay(self,rev):
        'This function help to find if the date is valid with a format of DDYY iinput'
        # transfer rev to an integer
        number = int(rev)
        # find the day
        d = number // 100
        # find the month
        m = number % 100
        # define a little month list for months that have 30 days
        littleMonth = [4,6,9,11]
        # for month not equal to 1 to 12 and day not equal to 1-31, return False
        if m > 12 or m < 1:
            return False
        if d > 31 or d < 1:
            return False
        # if Month is Feb, return True when day less than or equal to 28
        if m == 2:
            return (d <= 28)
        # if Month is in little month, return True when day less than or equal to 30
        if m in littleMonth :
            return (d <= 30)
        # all the other conditions, return True
        return True



date = Date()
date.getDate(2001,2100)
