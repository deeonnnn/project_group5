import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=FWCQ6BR9LLASNVQR'
r = requests.get(url)
data = r.json()

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

