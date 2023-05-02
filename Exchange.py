import requests

api_key = "d1d01af0db77065d19d8543a"
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"


def get_exchange_rate(base_currency, target_currency):
    response = requests.get(url + base_currency)
    data = response.json()
    if response.status_code == 200:
        base_rate = data["conversion_rates"][base_currency]
        target_rate = data["conversion_rates"][target_currency]
        return target_rate / base_rate
    else:
        raise Exception("Failed to retrieve exchange rates")


# Usage example
amount = float(input("Enter the amount in the base currency: "))
base_currency = input("Enter the base currency: ")
target_currency = input("Enter the target currency: ")

exchange_rate = get_exchange_rate(base_currency.upper(), target_currency.upper())
converted_amount = amount * exchange_rate
print(f"{amount:.2f} {base_currency.upper()} = {converted_amount:.2f} {target_currency.upper()}")
