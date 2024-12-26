"""
Ask user for a valid amount if invalid print error message
Ask user for source of currency if invalid print error message
Ask user for target currency if invalid print error message
"""
exchange_rate = {
    'USD': 1.0, 'EUR': 0.85, 'GBP': 0.75, 'INR': 74.0, 'AUD': 1.35, 'CAD': 1.25, 
    'SGD': 1.36, 'CHF': 0.92, 'MYR': 4.15, 'JPY': 110.0, 'CNY': 6.45
}

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
    source_currency = input('Enter the source currency (e.g. USD): ').upper()
    if source_currency not in currencies:
        print('Invalid source currency!')
    else:
        break

while True:
    target_currency = input('Enter the target currency (e.g. EUR): ').upper()
    if target_currency not in currencies:
        print('Invalid target currency!')
    else:
        break

converted_amount = amount * exchange_rate[source_currency] / exchange_rate[target_currency]
print(f'{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}')