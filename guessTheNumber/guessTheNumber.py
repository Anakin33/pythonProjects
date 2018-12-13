
import random

def getUserGuess():
    userGuess = input("What is my number? Must choose between 1-10. ")
    return int(userGuess)

def compareUserGuess():
    guess = getUserGuess()
    correct = generateRandomNumber()
    if(guess == correct):
        print("OMGGGGG YOU GUESSED it")
    elif (guess > 10 or guess < 1):
       print('You enter an invalid number... Try again pleeblet')

    else:
        print('You were wrong. Your number was', guess, 'and the correct number was', correct)


def generateRandomNumber():
    randomNum = random.randint(1, 10)
    return randomNum

#print(compareUserGuess())

'''

The Goal: Similar to the first project, this project also uses the random module in Python.
 The program will first randomly generate a number unknown to the user. The user needs to guess what that number is.
 (In other words, the user needs to be able to input information.)
  If the user’s guess is wrong, the program should return some sort of indication as to how wrong
  (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear.
  You’ll need functions to check if the user input is an actual number, to see the difference between the inputted number
   and the randomly generated numbers, and to then compare the numbers.

Concepts to keep in mind:

    Random function
    Variables
    Integers
    Input/Output
    Print
    While loops
    If/Else statements


Jumping off the first project, this project continues to build up the base knowledge and introduces
 user-inputted data at its very simplest.
With user input, we start to get into a little bit of variability.
'''