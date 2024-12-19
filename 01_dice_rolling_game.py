"""
Ask user if they want to play - yes/no
If yes they get two random numbers
If no the program terminates, and says thank you for playing
"""
import random

while True:
    answer = input("Roll the dice? (yes/no): ").lower()

    if answer == 'yes':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print(f'{dice1} and {dice2}')
    elif answer == 'no':
        print('Thank you for playing.')
        break
    else:
        print('Invalid input! Please enter yes or no.')