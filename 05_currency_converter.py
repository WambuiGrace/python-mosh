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


currencies = ('USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'SGD', 'CHF', 'MYR', 'JPY', 'CNY')
while True:
    source_currency = input('Enter the source currency: ')
    if source_currency not in currencies:
        print('Invalid source currency!')
    else:
        break

while True:
    target_currency = input('Enter the target currency: ')
    if target_currency not in currencies:
        print('Invalid target currency!')
    else:
        break


print(f'{amount} {source_currency} is equal to {amount} {target_currency}')