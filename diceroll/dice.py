from utils import *

re_rolls = r"([0-9]*d[0-9]*[dk]*[0-9]*)([+-][0-9]*)?([+-]?[0-9]*d[0-9]*[dk]*[0-9]*)?"
re_dice = r"([+-])?([0-9]*)(d)([0-9]+)([dk])?([0-9]+)?"
re_modifier = r"([-+][0-9]+)"

def rolldice(dicestring):
    diceroll = {
        'rolls': [],
        'total': 0
    }
    roll_list = []

    try:
        rolls = listfindall(re_rolls, dicestring)
    except IndexError:
        print("Incorrect Dice Format")
        return False

    for roll in rolls:
        try:
            roll_list.append(listfindall(re_dice,roll))
        except IndexError:
            roll_list.append(listfindall(re_modifier, roll))

    for roll in roll_list:
        if 'd' in roll:
            if roll[0] ==  '-' or roll[0] == '+':
                # for dice rolls after the first, to add or subtract
                temp_roll = roller(roll[1:])
                diceroll['rolls'].append(int(f'{roll[0]}{temp_roll}'))
            else:# rolling first dice rolls
                diceroll['rolls'].append(roller(roll))
        else:
            # rolls modifiers
            diceroll['rolls'].append(int(''.join(roll)))

    diceroll['total'] = sum(diceroll['rolls'])

    return diceroll


def statroller():
    return [roller("4d6k3") for i in range(6)]
