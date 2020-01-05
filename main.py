# A simple random number guessing game. Video 168 Pythom ZTM.
# System arguments when the script runs are integers
# Run from terminal DIR\main.py (start interger) (ending interger) e.g.python main.py 1 10

import sys
import random
import pyjokes
from colorama import Fore, Back, init
init()

print("")
print("Random Number Guessing Game")

guess = 0
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
n3 = random.randint(n1,n2)
print("")
joke = pyjokes.get_joke('en', 'neutral')
print(joke)
print("")
name = input("What is your name? ")

while guess != n3:
    try:
        guess = int(input(f"Enter a number between {n1} and {n2}: "))
    except ValueError:
        print(Fore.LIGHTRED_EX + "Enter a number only")
    if guess == n3:
        print()
        print(Fore.GREEN + f"You are right! Well done {name}")
    else:
        print()
        print(Fore.RED + "That answer is incorrect, try again.")
        print(Fore.RESET)


