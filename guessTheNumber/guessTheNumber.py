
import random

def get_user_guess():
    user_guess = input("What is my number? Must choose between 1-10. ")
    return int(user_guess)

def compare_user_guess():
    guess = get_user_guess()
    correct = generate_random_number()
    if (guess > 10 or guess < 1):
       print('You enter an invalid number... Try again pleeblet')
    elif (guess == correct):
        print("OMGGGGG YOU GUESSED it")
    else:
        print('You were wrong. Your number was', guess, 'and the correct number was', correct)


def generate_random_number():
    random_num = random.randint(1, 10)
    return random_num

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