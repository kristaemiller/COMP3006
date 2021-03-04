#Krista Miller
#3/4/2021

# *** HOW TO PLAY WAR DICE ***
# The game you will make is kind of like the card game war, only with dice instead of cards.
# The user will input how many dice they are rolling, and the number of sides on the dice.
# The player will start with a set amount of "money" (you can choose the amount).
# You will choose an amount you are betting on the next play
# You and a computer will both roll the amount of dice, and determine the winner (by sum of dice)
# You will gain or lose the money bet
# You will then choose to bet again or to cash out
# The game will continue until you cash out or are bankrupt.

import random

class Dice:
    #constructor
    def __init__(self, sides):
        if sides < 3:
            raise ValueError('A die cannot have less than 3 sides')
        self.sides = sides
        self.current = self.roll()

    def roll(self):
        self.current = random.randint(1, self.sides)
        return self.current

    def __str__(self):
        return str(self.current)

    #comparison methods
    def __lt__(self, other):
        return self.current < other.current

    def __le__(self, other):
        return self.current <= other.current

    def __gt__(self, other):
        return self.current > other.current

    def __ge__(self, other):
        return self.current >= other.current

    def __eq__(self, other):
        return self.current == other.current

    def __ne__(self, other):
        return self.current != other.current

    def __add__(self, other):
        if isinstance(other, int): #reference 1
            return other + self.current
        elif isinstance(other, Dice):
            return self.current + other.current
        raise ValueError("Not a die")

    def __radd__(self, other): #reference 2
        return self + (other)

#testing dice constructor
# MyDice= Dice(5)
# ComputerDice= Dice(6)
# print(MyDice.roll())
# print(ComputerDice.roll())
# print(MyDice.roll() < ComputerDice.roll())
# print(MyDice.roll() == ComputerDice.roll())
# dice_list = [Dice(6), Dice(10)]
# print(dice_list)

class CupOfDice:
    #constructor
    def __init__(self, sides, numDice):
        self.numDice = numDice
        self.dice = [Dice(sides) for i in range(numDice)]

    def sum(self):
        return sum(self.dice)

    #comparison methods
    def __lt__(self, other):
        return self.sum() < other.sum()

    def __le__(self, other):
        return self.sum() <= other.sum()

    def __gt__(self, other):
        return self.sum() > other.sum()

    def __ge__(self, other):
        return self.sum() >= other.sum()

    def __eq__(self, other):
        return self.sum() == other.sum()

    def __ne__(self, other):
        return self.sum() != other.sum()

    def __str__(self):
        return ", ".join([str(d) for d in self.dice]) #reference 3

    def roll(self):
        for die in self.dice:
            die.roll()

def main():
    """runs the dice game"""
    TOTAL_MONEY= 10

    #user inputs how many dice they are rolling, and the number of sides of the dice
    num_dice = int(input("How many dice: "))
    num_sides = int(input("How many sides: "))

    player_cup = CupOfDice(num_sides, num_dice)
    computer_cup = CupOfDice(num_sides, num_dice)

    player_money = TOTAL_MONEY

    #make bet
    while player_money > 0:
        bet = None
        while bet is None:
            try:
                bet = int(input(f"What will you bet (You have ${player_money})? "))
                if bet > player_money:
                    print(f"You don't have enough to make that bet.  Please input number <= ${player_money}")
                    bet = None
            except ValueError:
                bet = None

    #roll dice with Cup of Dice
        player_cup.roll()
        computer_cup.roll()

        print(f"Player cup: {player_cup}, total sum: ${player_cup.sum()}")
        print(f"Computer cup: {computer_cup}, total sum: ${computer_cup.sum()}")

    #compare rolls
        if player_cup < computer_cup:
            player_money -= bet
            print(f"You lost, your money is ${player_money}")
        elif player_cup > computer_cup:
            player_money += bet
            print(f"You won, your total money is now ${player_money}")

    #continue play or break
        if player_money and input("Would you like to cash out (y/n)? ").lower() == 'y':
            break

main()

#References:
#1: https://www.w3schools.com/python/ref_func_isinstance.asp
#2: https://stackoverflow.com/questions/9126766/addition-between-classes-using-radd-method
#3: https://stackoverflow.com/questions/1876191/what-exactly-does-the-join-method-do
