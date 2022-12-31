# Script accepts input, format should be: python3 domains.py keyword

import requests
import json
import sys

unavail = 'AVAILABILITY_UNAVAILABLE'

headers = {
    'authority': 'domains.google.com',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36',
    'content-type': 'application/json',
    'sec-gpc': '1',
    'origin': 'https://domains.google.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'accept-language': 'en-US,en;q=0.9',
}

data = '{"clientFilters":{},"clientUserSpec":{"countryCode":"US","currencyCode":"USD","sessionId":"2209096463072398972"},"debugType":"DEBUG_TYPE_NONE","query":"' + str(sys.argv[1]) + '"}'
response = requests.post('https://domains.google.com/v1/Main/FeSearchService/AllTlds', headers=headers, data=data)
clean_response = (response.text.replace(")]}'", ''))
domains = json.loads(clean_response)

results = domains['allTldsResponse']['results']['result']

for k in results:
    domainResult = k['domainName']
    sld = k['domainName']['sld']
    tld = k['domainName']['tld']
    rebuiltDomain = sld + '.' + tld
    availResult = k['supportedResultInfo']['availabilityInfo']['availability']

    if availResult == unavail:
        print(rebuiltDomain + " is Unavailable")
        print("----------")
    elif availResult != unavail:
        print(rebuiltDomain + " CAN BE PURCHASED!")
        print("----------")

