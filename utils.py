import re, random, heapq


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
    amount = int(roll[0])
    sides = int(roll[2])
    keep_drop = ""
    keep_drop_amount = 0
    rolls = []
    all_rolls = []

    # checks to see if there is a keep or drop requirment
    if len(roll) > 3:
        try:
            keep_drop = roll[3].lower()
            keep_drop_amount= int(roll[4])

            if keep_drop_amount > amount:
                print("Keeping or dropping too many die")
                return False

        except IndexError:
            print("No number after keep or drop")
            return False

    for num in range(amount):
        rolls.append(random.randint(1, sides))
    if keep_drop == 'k':
        all_rolls = heapq.nlargest(keep_drop_amount, rolls)
    elif keep_drop == 'd':
        all_rolls = heapq.nsmallest(keep_drop_amount, rolls)
    else:
        all_rolls = rolls

    return sum(all_rolls)