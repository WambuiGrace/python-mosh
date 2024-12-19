"""
Generate a random number from (1, 100)
Loop
    Ask user to guess the number
    if not a valid number, print an error message
    if the number < guess, print 'too low'
    if the number > guess, print 'too high'
    Else print 'You guessed it!'
"""
import random
# Number the user should guess
number = random.randint(1, 100)

while True:
    try:
        guess = int(input('Guess a number between 1 and 100: '))

        if guess < number:
            print('Too low, go higher')
        elif guess > number:
            print('Too high, go lower')
        else:
            print('You guessed it!')
            break
    except ValueError:
        print('Enter a valid number')
    
