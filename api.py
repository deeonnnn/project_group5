import requests
from pathlib import Path
import csv
import json

home = Path.home()
print(home)

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=FWCQ6BR9LLASNVQR"
function= "CURRENCY_EXCHANGE_RATE"
from_currency = "USD"
to_currency ="SGD"
response = requests.get(url)
print(response)
data = response.json()
print(data)

{
    "Realtime Currency Exchange Rate": {
        "1. From_Currency Code": "USD",
        "2. From_Currency Name": "United States Dollar",
        "3. To_Currency Code": "SGD",
        "4. To_Currency Name": "Singapore Dollar",
        "5. Exchange Rate": "1.38861000",
        "6. Last Refreshed": "2022-07-27 16:23:46",
        "7. Time Zone": "UTC",
        "8. Bid Price": "1.38861000",
        "9. Ask Price": "1.38861000",
    }
}



url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=FWCQ6BR9LLASNVQR'
request = requests.get(url)
data = request.json()
import json
# print(json.dumps(data["Time Series FX (Weekly)"],indent=4))
newdata=data["Time Series FX (Weekly)"]
empty_list = []
for item in newdata:
    empty_list.append(newdata[item]["4. close"])

for i in range(0, len(empty_list)):
    empty_list[i] = float(empty_list[i])
# print(json.dumps(empty_list,indent=4))
# print(empty_list)

weekly_average=sum(empty_list) / len(empty_list)
print(weekly_average)

