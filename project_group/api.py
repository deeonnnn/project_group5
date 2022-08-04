import requests

def api_function():

    """
     This function makes an API call to https://www.alphavantage.co
     to extract the real time exchange rate (Forex) in JSON
     output 
    """
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=FWCQ6BR9LLASNVQR"
    # function= "CURRENCY_EXCHANGE_RATE"
    # from_currency = "USD"
    # to_currency ="SGD"
    response = requests.get(url)
    # if api call is successful, response.status code=200, we can return the extracted coversion rate
    if response.status_code == 200:
        data = response.json()
        convrate=data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        convrate=float(convrate)
        return convrate
    # if api call is not successful, response.status code is not 200, we return API REQUEST ERROR FOUND
    # this lets the main function know there is an error to prevent a crash
    else:
        return "API REQUEST ERROR FOUND"

