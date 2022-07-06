import requests
import json
from datetime import datetime
import pdb 

def get_currency_prices():
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
        'Upgrade-Insecure-Requests': '100',
        'Cache-Control': 'no-cache',
        'Connection': 'close',
    }



    url='https://call5.tgju.org/ajax.json?rev=cuL8G3eIsub5vXsO3YzNAOKSoPmMrS1M35ZZ94mNaRh4ZUT5U43ghlOQQOJ3'
    data = requests.get(url,headers=header).text

    data = json.loads(data)
    prices = data.get('current')

    geram18 = prices.get('geram18', 'none')
    geram24 = prices.get('geram24', 'none')
    gold_740k = prices.get('gold_740k', 'none')
    gold_melted_transfer = prices.get('gold_melted_transfer', 'none')

    coin_emami = prices.get('sekee', 'none')
    coin_bahar_azadi = prices.get('sekeb', 'none')
    coin_half = prices.get('retail_nim', 'none')
    coin_quarter = prices.get('retail_rob', 'none')
    coin_gerami = prices.get('retail_gerami', 'none')

    currency = {
        'carat18': geram18['p'],
        'carat24': geram24['p'],
        'carat740': gold_740k['p'],
        'melted_gold_transfer': gold_melted_transfer['p'],
        'coin_emami': coin_emami['p'],
        'coin_bahar_azadi': coin_bahar_azadi['p'],
        'half_coin': coin_half['p'],
        'quarter_coin': coin_quarter['p'],
        'gerami_coin': coin_gerami['p']
    }

    
    return currency



if __name__=='__main__':
    data=get_currency_prices()
    pdb.set_trace()