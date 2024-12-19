"""
Take user input in the form of rock, paper, or scissors represented by r/p/s
Computer makes a random choice
Determine a winner based on the rules of rock, paper, scissors
Print the result
Ask the user if they want to play again
"""

import random


emojis = {'rock': '🪨', 'paper': '📃', 'scissors': '✂️' }
choices = ('rock', 'paper', 'scissors')

while True:
    user_choice = input('Rock, Paper, Scissors? ').lower()
    if user_choice not in choices:
        print('Invalid choice, try again')
        continue

    computer_choice = random.choice(choices)

    print(f'You chose: {emojis[user_choice]}')
    print(f'Computer chose: {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('It/s a tie')
    elif(
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')):
        print('You win')
    else:
        print('Computer wins')

    should_continue = input('Continue with the game? (y/n): ').lower()
    if should_continue == 'n':
        break