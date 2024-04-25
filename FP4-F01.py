# - FP4-F01 Simple OOP - #
# - Xzavier Moosomin - #
# - 04/25/2024 - #

# - Developer Notes - #
# this oop stuff is hard to wrap my head around
# spend a quicky on it
# roughly half an hour, but that doesnt sound too bad
# for someone to start learning it
# not gonna lie i might be kinda smart

# im gonna need some help on inheritance if im gonna be needing that

# - Classes - #

class Man:
    def __init__(self, person, age, height, sport, goalamt, scoresamt ):
        self.person = person
        self.age = age
        self.height = height
        self.sport = sport
        self.goalamt = goalamt
        self.scoresamt = scoresamt
        
    def createman(self): # OH MY GOD I AM LEARNING
        print("Apparently, I am", self.person)
        print("And I am", self.age, "years old.")
        print("My height is", self.height,".")
        print("I also play", self.sport, "professionally.")

# - Code - #
# make a man
personchoice = input("Who are we talking about?\n>")

makeage = int(input(f"How old is {personchoice}?\n>"))

makeheight = input(f"How tall is {personchoice}?\n>")

makesport = input(f"What sport does {personchoice} play?\n>")

goals = int(input("How many goals did he let in?\n>"))
scores = int(input("How many scores did he make on the other team?\n>"))

human = Man(personchoice, makeage, makeheight, makesport, goals, scores) # set variables

human.createman() # print out what you made
