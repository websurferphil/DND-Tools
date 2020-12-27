import re
import random

def errortest(name, desc):
    # Error Testing funciton

    # Name could be name of variable,  or whatever helps dial down on an error
    # desc could be the value or type of a variable or even location
    print("########################")
    print("{:s}: {:s}".format(name, str(desc)))
    print("########################")

def listfindall(reg, text):
    # turns find all into a list
    return list(filter(None,re.findall(reg, text)[0]))

def roller(roll):
    errortest("number of dice to roll", roll[0])
    errortest("number of sides on dice", roll[2])
    amount = int(roll[0])
    sides = int(roll[2])


    rolltotal = 0

    # checks to see if there is a keep or drop requirment
    if len(roll) > 3:
        print("Has a keep or drop")
        try:
            if roll[3] is "k":
                errortest("Keep the highest",roll[4])
            if roll[3] is "d":
                errortest("Drop lowest", roll[4])
        except IndexError:
            print("No number after keep or drop")
            return False

    for num in range(amount):
        rolltotal += random.randint(1, sides)

    print(rolltotal)

    return "Hello"