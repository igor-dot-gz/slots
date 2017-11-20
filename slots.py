# coding: utf-8
import random
import secrets
from time import sleep
import os

i = 1
wins = []
temp = 0

burger, banana, cherry, gold, seven = 1, 10, 100, 1000, 10000
two_multi, three_multi = 5, 20
bets = 0
betadd
balance = 100
earn = 0
casino_bal = 1000000.00
casino_earn = 0

burger_chance_low = 20
banana_chance_low = 15
cherry_chance_low = 10
gold_chance_low = 5
seven_chance_low = 1

burger_chance_med = 20
banana_chance_med = 15
cherry_chance_med = 15
gold_chance_med = 10
seven_chance_med = 2

burger_chance_high = 20
banana_chance_high = 15
cherry_chance_high = 10
gold_chance_high = 10
seven_chance_high = 3

'''
machine = slots(X)
x can equal "low", "med" or "high"
'''

class slots:

    def __init__(self, chance="med"):
        self.chance = chance

    def spin():

        if bets <= 0:
            raise error

        os.system('cls')

        wins = []
        spin1 = 0
        spin2 = 0
        spin3 = 0

        if chance == "low":
            for i in burger_chance_low:
                wins.append("burger")
            for i in banana_chance_low:
                wins.append("banana")
            for i in cherry_chance_low:
                wins.append("cherry")
            for i in gold_chance_low:
                wins.append("gold")
            for i in seven_chance_low:
                wins.append("seven")

        if chance == "med":
            for i in burger_chance_med:
                wins.append("burger")
            for i in banana_chance_med:
                wins.append("banana")
            for i in cherry_chance_med:
                wins.append("cherry")
            for i in gold_chance_med:
                wins.append("gold")
            for i in seven_chance_med:
                wins.append("seven")

        if chance == "high":
            for i in burger_chance_high:
                wins.append("burger")
            for i in banana_chance_high:
                wins.append("banana")
            for i in cherry_chance_high:
                wins.append("cherry")
            for i in gold_chance_high:
                wins.append("gold")
            for i in seven_chance_high:
                wins.append("seven")

        for i in len(wins):
            random.shuffle(wins)

        spin1 = secrets.choice(wins)
        spin2 = wins[secrents.randbelow(len(wins)-1)]
        spin3 = wins[random.randint(0, len(wins)-1)]

        print(spin1)
        print(spin2)
        print(spin3)
        print("")

        if spin1 == "burger":
            spin1 = burger
        elif spin1 == "banana":
            spin1 = banana
        elif spin1 == "cherry":
            spin1 = cherry
        elif spin1 == "gold":
            spin1 = gold
        elif spin1 == "seven":
            spin1 = seven

        if spin2 == "burger":
            spin2 = burger
        elif spin2 == "banana":
            spin2 = banana
        elif spin2 == "cherry":
            spin2 = cherry
        elif spin2 == "gold":
            spin2 = gold
        elif spin2 == "seven":
            spin2 = seven

        if spin3 == "burger":
            spin3 = burger
        elif spin3 == "banana":
            spin3 = banana
        elif spin3 == "cherry":
            spin3 = cherry
        elif spin3 == "gold":
            spin3 = gold
        elif spin3 == "seven":
            spin3 = seven

        spin_total = spin1 + spin2 + spin3

        if spin1 == spin2 and spin1 != spin3:
            spin_total = spin_total * two_multi
        elif spin1 == spin3 and spin1 != spin2:
            spin_total = spin_total * two_multi
        elif spin2 == spin3 and spin2 != spin1:
            spin_total = spin_total * two_multi
        elif spin1 == spin2 and spin1 != spin3:
            spin_total = spin_total * two_multi
        elif spin1 == spin2 and spin2 == spin3:
            spin_total = spin_total * three_multi

        casino_earn = spin_total

        print("Gain: £" + str(spin_total))
        print("Bet Balance: £" + str(bets))
        print("Your Balance: £" + str(balance))



    def bet(betadd=0):
        temp = balance - betadd
        if temp < 0:
            raise error
        else:
            pass
        balance = temp
        bets += betadd
        temp = 0
        betadd = 0
