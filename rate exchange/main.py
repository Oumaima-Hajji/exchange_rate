"""
Script to convert Euro to MAD
"""
from lib2to3.pygram import Symbols
import requests


URL = "https://api.exchangerate.host/latest"


def euro_to_dirham(amount):

    """
    Function to convert Euro to MAD
    """
    response = requests.get(URL , params= { "base": "EUR" , "symbols": "MAD", "amount": amount })
    data = response.json()
    data_rates = data['rates']
    mad_rates = data_rates['MAD']
    return mad_rates


result = euro_to_dirham(1000000)

print(result)
