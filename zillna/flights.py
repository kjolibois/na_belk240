from pprint import pprint

import requests

import json



r = requests.get( headers = {'User-agent': 'flightdealsearcher'} ,url='http://www.reddit.com/r/atlanta/search.json?q=flight%20deals&restrict_sr=1&sort=new')

r.text

data = r.json()
pprint(data)
