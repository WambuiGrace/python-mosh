"""
Ask user for a valid amount if invalid print error message
Ask user for source of currency if invalid print error message
Ask user for target currency if invalid print error message
"""

while True:
    try:
        amount = float(input('Enter the amount: '))
        if amount <= 0:
            raise ValueError
        break
    except ValueError:
        print('Invalid amount!')