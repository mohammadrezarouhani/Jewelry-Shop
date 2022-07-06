import requests
import json
from datetime import datetime
import pdb 

def get_currency_prices():
    header = {
        'date': 'Tue, 05 Jul 2022 18:37:52 GMT',
        'content-type': 'application/json',
        'last-modified': 'Tue, 05 Jul 2022 18:37:48 GMT',
        'etag': "W/62c484fc-2b3ba",
        'expires': 'Thu, 31 Dec 2037 23:55:55 GMT',
        'cache-control': 'public, max-age=315360000',
        'access-control-allow-origin':'*',
        'cf-cache-status':'MISS',
        'expect-ct': 'max-age=604800; report-uri=https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct',
        'report-to': {"endpoints":[{"url":"https:\/\/a.nel.cloudflare.com\/report\/v3?s=PuPc%2B4Y9Pue3Dh1%2B9ZeC43cT%2Frjw4WzjdnP0UPeSPPHYZmgNMgaD5JCm1km73SSw%2B50fymnZ02f9L9scbicU5pJKzwm5jZSppoqx9q6TbS2x%2B%2Bi0IliHRvF6yIJNgKZC"}],"group":"cf-nel","max_age":604800},
        'nel': {"success_fraction":0,"report_to":"cf-nel","max_age":604800},
        'vary': 'Accept-Encoding',
        'strict-transport-security': 'max-age=15552000; includeSubDomains; preload',
        'x-content-type-options': 'nosniff',
        'server': 'cloudflare',
        'cf-ray': '726236e2d8a18fe3-FRA',
        'content-encoding': 'br',
        'alt-svc': 'h3=":443"; ma=86400, h3-29=":443"; ma=86400',
    }



    url='https://call5.tgju.org/ajax.json?rev=cuL8G3eIsub5vXsO3YzNAOKSoPmMrS1M35ZZ94mNaRh4ZUT5U43ghlOQQOJ3'
    data = requests.get(url,headers=header).text

    data = json.loads(data)
    prices = data.get('current')

    geram18 = prices.get('geram18', 'none')
    geram24 = prices.get('geram24', 'none')
    gold_740k = prices.get('gold_740k', 'none')

    dollor = prices.get('price_dollar_rl', 'none')
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
        'dollor': dollor['p'],
        'melted_gold_transfer': gold_melted_transfer['p'],
        'coin_emami': coin_emami['p'],
        'coin_bahar_azadi': coin_bahar_azadi['p'],
        'half_coin': coin_half['p'],
        'quarter_coin': coin_quarter['p'],
        'gerami_coin': coin_gerami['p']
    }
    pdb.set_trace()    
    
    return currency



if __name__=='__main__':
    data=get_currency_prices()