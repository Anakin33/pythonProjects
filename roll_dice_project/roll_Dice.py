'''
The Goal: Like the title suggests, this project involves writing a program that simulates rolling dice.
When the program runs, it will randomly choose a number between 1 and 6.
(Or whatever other integer you prefer — the number of sides on the die is up to you.) The program will print what that number is.
It should then ask you if you’d like to roll again.
For this project, you’ll need to set the min and max number that your dice can produce. For the average die, that means a minimum of 1 and a maximum of 6.
You’ll also want a function that randomly grabs a number within that range and prints it.

Concepts to keep in mind:

    Random
    Integer
    Print
    While Loops
'''
import random

def should_roll (input: bool) -> int:
    if input == True:
        num = str(roll_dice())
        print(f'Your roll is {num}. Would you like to roll again?')

    else:
        print("game over bitches")

def roll_dice():
    return random.randint(1, 6)


if __name__ == '__main__':
    should_roll(True)