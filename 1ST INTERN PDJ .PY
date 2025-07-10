
# currency CONVERTER

exchange_rates = {
    'USD': 1.0,
    'EUR': 0.85,
    'INR': 74.5,
    'GBP': 0.75,
    'JPY': 110.0,
    'CAD': 1.25
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return None
    usd_amount = amount / exchange_rates[from_currency]
    converted_amount = usd_amount * exchange_rates[to_currency]
    return round(converted_amount, 2)

def main():
    print("Currency Converter App (CLI)")
    print("Supported currencies:", ', '.join(exchange_rates.keys()))

    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From Currency (e.g. USD): ").upper()
        to_currency = input("To Currency (e.g. INR): ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        if result is not None:
            print(f"{amount} {from_currency} = {result} {to_currency}")
        else:
            print("Error: Unsupported currency code entered.")
    except ValueError:
        print("Invalid input. Please enter numeric amount.")

if __name__ == "__main__":
    main()
    
