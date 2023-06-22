import json
from typing import Final
import requests

# constants
base_url: Final[str] = 'https://api.apilayer.com/exchangerates_data/latest/'
api_key: Final[str] = 'vttpOJL5KSvkYLuB8cB6Tn9N8vuwd1KZ'

def get_rates(mock: bool= False) -> dict:
    if mock:
        with open('rates.json', 'r') as file:
            return json.load(file)

    payload: dict = {'access_key': api_key}
    request = requests.get(url=base_url, params=payload)
    data : dict = request.json()

    with open('rates.json', 'w') as file:
        json.dump(data, file)

    return data

def get_currency(currency: str, rates: dict) -> float:
    currency: str = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f'"{currency}" is a not a valid currency')


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)
    conversion: float = round((vs_rate / base_rate) * amount, 2)
    print(f'{amount:,.2f} ({base}) is: {conversio:,.2f}  ({vs}')
    return conversion

def main():
    data: dict = get_rates(moch = True)
    rates: dict = data.get('rates')
    convert_currency(100, 'EUR', 'JPY', rates = rates)

if __name__ == '__main__':
    main()
