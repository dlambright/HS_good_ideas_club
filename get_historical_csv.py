import json
import requests
import time
import datetime
from collections import namedtuple

url = "https://api.coinmarketcap.com/v1/ticker/ripple/"

for i in range(0,1000):
    myResponse = requests.get(url)
    #print myResponse.json()
    
    if (myResponse.json) > 1:
    
    	asdf = myResponse.json()[0]
    	fdsa = float(asdf["price_usd"])

    	with open('values/values.csv', 'a+') as outFile:
            outFile.write(str(datetime.datetime.now()) + ", " + str(fdsa) + "\n")
    	print datetime.datetime.now()
    	print i
    time.sleep(300)






