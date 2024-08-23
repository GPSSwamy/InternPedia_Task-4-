import requests

def get_exchange_rates(api_key):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['conversion_rates']
    else:
        print("Error fetching exchange rates. Please check your API key and try again.")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == to_currency:
        return amount
    base_amount = amount / rates[from_currency]
    return base_amount * rates[to_currency]

def display_conversion(amount, from_currency, to_currency, converted_amount):
    print(f'{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}')

def main():
    api_key = '6d770f86065f13baeaeb7c41'
    rates = get_exchange_rates(api_key)

    if rates is None:
        return

    currencies = list(rates.keys())
    while True:
        print("\nAvailable currencies:", ', '.join(currencies))
        from_currency = input("Enter the source currency code: ").upper()
        to_currency = input("Enter the target currency code: ").upper()

        if from_currency not in currencies or to_currency not in currencies:
            print("Invalid currency code. Please try again.")
            continue

        try:
            amount = float(input(f"Enter the amount in {from_currency}: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        converted_amount = convert_currency(amount, from_currency, to_currency, rates)
        display_conversion(amount, from_currency, to_currency, converted_amount)

        cont = input("Do you want to perform another conversion? (yes/no): ").lower()
        if cont != 'yes':
            break
main()