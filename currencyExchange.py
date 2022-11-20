import requests
import json

currencyFrom = input('What currency are you converting from? Default, EUR ')
amount = float(input('How much are you converting? '))
currencyTo = input('What currency are you converting to? ')

req = requests.get('https://api.exchangerate.host/latest?base='+currencyFrom)
data = req.json()
rate = data['rates'][currencyTo]
result = amount*rate
print("{:.2f}".format(amount),currencyFrom,'is equal to',"{:.2f}".format(result),currencyTo)
