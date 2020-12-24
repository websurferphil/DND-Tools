import re

a = "Hello"
re_rolls = r"(([0-9]*d[0-9]*[dk]*[0-9]*)([+-][0-9]*)?([+-]?[0-9]*d[0-9]*[dk]*[0-9]*)?)"
re_numbers = r""

def rolldice(dicestring):
    rolls = list(re.findall(re_rolls, dicestring)[0])
    rolls.pop(0)

    splitrolls = list(re.findall(re_numbers),)

    return rolls
