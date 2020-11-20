#Assignment 0801 Plot Generator AND 0802 Plot Viewer
#Dawei Wang May.26,2020
#YouTube Video Link: https://youtu.be/0l2cXdzi4c4 and https://youtu.be/SeU9WZYOrdg  
#I have not given or received any unauthorized assistance on this assignment.
import random

class SimplePlotGenerator:
    'A class that could generate the plot'
    def __init__(self):
        'The constractor that defines file storage directory and all files path'
        self.path = r'C:\Users\rocke\iCloudDrive\Desktop\DSC430\Week 8\Assignment'
        self.plot_names = self.path + '\plot_names.txt' 
        self.plot_adjectives = self.path + '\plot_adjectives.txt'
        self.plot_profesions = self.path + '\plot_profesions.txt'
        self.plot_verbs = self.path + '\plot_verbs.txt'
        self.plot_adjectives_evil = self.path + '\plot_adjectives_evil.txt'
        self.plot_villian_job = self.path + '\plot_villian_job.txt'
        self.plot_villains = self.path + '\plot_villains.txt'

    def registerPlotViewer(self,pv):
        'The register that provoide Plot Viewer an attribute to opearte'
        self.pv = pv

    def generate(self):
        'generate something'
        return "Something happens"

    def randomplot(self,file):
        'a function to get random plot in a plot file'
        # open the file and read all lines and store it in list without 
        # \n or \t in the end, then close the file, find the length of list
        infile = open(file)
        list = infile.read().splitlines()
        infile.close
        leng = len(list)
        # return a random element in the list 
        return list[random.randint(0,leng-1)]

class RandomPlotGenerator(SimplePlotGenerator):

    def generate(self):
        'Generate a random plot by using plot files and randomplot function'
        result = "{}, a {} {}, must {} the {} {}, {}.".format(self.randomplot(self.plot_names), \
            self.randomplot(self.plot_adjectives), self.randomplot(self.plot_profesions), \
            self.randomplot(self.plot_verbs), self.randomplot(self.plot_adjectives_evil), \
            self.randomplot(self.plot_villian_job),self.randomplot(self.plot_villains))
        return result
        
class InteractivePlotGenerator(SimplePlotGenerator):

    def generate(self):
        'Provide 5 random options for user and generate a random plot that user likes'
        # introduction
        self.pv.displayReminders("Let's generate a plot that you like!\
        \nYou will choose any plot you want in the list given and you will get your own plot~\n ")

        # generate a list that contains 5 random names, give the options and ask for the selection
        # the first part of our result op1 will be selected name in the list 
        # apply this design and find all 7 parts of the result

        self.pv.displayReminders("Chose a hero's name from the following list:")
        names = []
        for i in range(5):
            names.append(self.randomplot(self.plot_names))
        self.pv.displayOptions(names)
        op1 = names[int(self.pv.queryUser("\nWhich one of the names listed above do you want? \
        \nEnter the index of name you want:\n")) -1]

        # select random adjectives and start display the current result after each selection 
        self.pv.displayReminders("Chose a description for your hero from the following list:")
        adj = []
        for i in range(5):
            adj.append(self.randomplot(self.plot_adjectives))
        self.pv.displayOptions(adj)
        op2 = adj[int(self.pv.queryUser("\nWhich one of the adjectives listed above do you want? \
        \nEnter the index of name you want:\n")) -1]
        self.pv.displayReminders("Now we have:\n{}, a {}\n".format(op1,op2))

        # select random profesions and display the current result
        self.pv.displayReminders("Chose a profesion for your hero from the following list:")
        profesions = []
        for i in range(5):
            profesions.append(self.randomplot(self.plot_profesions))
        self.pv.displayOptions(profesions)
        op3 = profesions[int(self.pv.queryUser("\nWhich one of the profesions listed above do you want? \
        \nEnter the index of name you want:\n")) -1]
        self.pv.displayReminders("Now we have:\n{}, a {} {},\n".format(op1,op2,op3))

        # select random verbs and display the current result
        self.pv.displayReminders("Chose an action for your hero from the following list:")
        verbs = []
        for i in range(5):
            verbs.append(self.randomplot(self.plot_verbs))
        self.pv.displayOptions(verbs)
        op4 = verbs[int(self.pv.queryUser("\nWhich one of the verbs listed above do you want? \
        \nEnter the index of name you want:\n")) -1]
        self.pv.displayReminders("Now we have:\n{}, a {} {}, must {}\n".format(op1,op2,op3,op4))

        # select random adjectives for evil and display the current result
        self.pv.displayReminders("Chose a description for the evil from the following list:")
        adj_evil = []
        for i in range(5):
            adj_evil.append(self.randomplot(self.plot_adjectives_evil))
        self.pv.displayOptions(adj_evil)
        op5 = adj_evil[int(self.pv.queryUser("\nWhich one of the adj for evil listed above do you want? \
        \nEnter the index of name you want:\n")) -1]
        self.pv.displayReminders("Now we have:\n{}, a {} {}, must {} the {} ,\n".format(op1,op2,op3,op4,op5))

        # select random villian's job and display the current result
        self.pv.displayReminders("Chose a job for villain from the following list:")
        villian_job = []
        for i in range(5):
            villian_job.append(self.randomplot(self.plot_villian_job))
        self.pv.displayOptions(villian_job)
        op6 = villian_job[int(self.pv.queryUser("\nWhich one of the job listed above do you want? \
        \nEnter the index of name you want:\n")) -1]
        self.pv.displayReminders("Now we have:\n{}, a {} {}, must {} the {} {},\n".format(op1,op2,op3,op4,op5,op6) )

        # select random villains and reminder user to check the final result
        self.pv.displayReminders("Chose a name for villain from the following list:")
        villains = []
        for i in range(5):
            villains.append(self.randomplot(self.plot_villains))
        self.pv.displayOptions(villains)
        op7 = villains[int(self.pv.queryUser("\nWhich one of the villains listed above do you want? \
        \nEnter the index of name you want:\n")) -1]
        self.pv.displayReminders("\nYou got it, here's your own plot:\n" )

        # return the result in this format
        return "{}, a {} {}, must {} the {} {}, {}.".format(op1,op2,op3,op4,op5,op6,op7)


class PlotViewer:
    'The viewer and controller of plot generator'

    def registerPlotGenerator(self,pg):
        'the function that registers the generator'
        self.pg = pg
        self.pg.registerPlotViewer(self)

    def queryUser(self,str):
        'the function that query user'
        return input(str)

    def displayReminders(self,str):
        'the function that display system reminders'
        print(str)

    def displayOptions(self,list):
        'the function that display optins in this format'
        print('Options are:\n1.{}  2.{}  3.{}  4.{}  5.{}'.format(list[0],list[1],list[2],list[3],list[4]))

    def generate(self):
        'the function that controls generation'
        print(self.pg.generate())


def main():
    'The main function that present all classes and functions above'
    # start a Viewer 
    pv = PlotViewer()
    print("\nLogged in to the plot generator\nAttempting the simple plot generator ...\n")
    # attempt Simple generator
    pv.registerPlotGenerator(SimplePlotGenerator())
    pv.generate()

    # attempt Random generator
    print("\n\nAttempting the random plot generator ...\n")
    pv.registerPlotGenerator(RandomPlotGenerator())
    pv.generate()

    # attempt Random generator
    print("\n\nAttempting the interactive plot generator ...\n")
    pv.registerPlotGenerator(InteractivePlotGenerator())
    pv.generate()

    # print terminated reminder
    print("Thanks for using, service terminated")


main()

input("你要多大杯")
