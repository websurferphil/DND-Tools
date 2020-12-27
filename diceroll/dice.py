from utils import *

re_rolls = r"([0-9]*d[0-9]*[dk]*[0-9]*)([+-][0-9]*)?([+-]?[0-9]*d[0-9]*[dk]*[0-9]*)?"
re_dice = r"([+-])?([0-9]*)(d)([0-9]+)([dk])?([0-9]+)?"
re_modifier = r"([-+][0-9]+)"

def rolldice(dicestring):

    print(dicestring)

    try:
        rolls = listfindall(re_rolls, dicestring)
    except IndexError:
        print("Incorrect Dice Format")
        return False

    roll_list = []

    for roll in rolls:
        try:
            roll_list.append(listfindall(re_dice,roll))
        except IndexError:
            roll_list.append(listfindall(re_modifier, roll))

    for roll in roll_list:
        if 'd' in roll:
            roller(roll)
        else:
            print("Modifier Roll")

    return False
