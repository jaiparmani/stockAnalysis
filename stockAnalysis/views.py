from django.shortcuts import render
from django.http import HttpResponse
from .forms import StockExchangeForm
# Create your views here.
# https://twelvedata.com/docs#stocks-list

import requests
def stockList(request):
    if(request.method=="POST"):
        form = StockExchangeForm(request.POST)
        if(form.is_valid()):
            # StockExchange
            exchange=form.data["exchange"]
            print(exchange)
            print("https://api.twelvedata.com/stocks?exchange="+exchange+"&outputsize=12&source=docs")
            url="https://api.twelvedata.com/stocks?exchange="+exchange+"&outputsize=12&source=docs"
            print(url   )
            response = requests.get(url)
        # print(response.json())
            
            stocks = response.json()
            print(stocks)
            return render(request, "stockList.html" ,{"stocks":stocks["data"],"form":form})   
        else:
            print("FORM is not valid")
    else:

        form = StockExchangeForm()
        response = requests.get("https://api.twelvedata.com/stocks?exchange=BSE&outputsize=12&source=docs")
        stocks = response.json()

        return render(request, "stockList.html" ,{"stocks":stocks["data"], "form":form})  



def stockDetail(request, symbol):
    # response = requests.get("https://api.twelvedata.com/stocks?symbol={}&exchange=BSE&outputsize=12&source=docs".format(symbol))
    # print("https://api.twelvedata.com/stocks?symbol={}&exchange=BSE&outputsize=12&source=docs".format(symbol))
    # print(response)
    # stock = response.json()

    # print(response)
    # for i in response:
    #     print(i)
    # return HttpResponse(response)
    from twelvedata import TDClient
    # td = TDClient(apikey="d44fa7950a544ef799b5d5353c54feb9")
    # ts = td.time_series(
    # symbol=symbol   ,
    # interval="5min"
    # ).as_json() 

    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BSE%3A{}&apikey=ERBV9KAAJRYRXOVG".format(symbol))
    print("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BSE%3A{}&apikey=ERBV9KAAJRYRXOVG".format(symbol))
    print(response)
    stock = response.json()
    # for i in stocks:
    #     print(i)
    # print(stock['Time Series (Daily)'])
    data = stock['Time Series (Daily)']

    return HttpResponse(stock["Time Series (Daily)"])
    return render(request, "stockDetail.html" ,{"stock":stock["data"][0]})   


    # https://api.polygon.io/v1/open-close/AAPL/2021-04-06?unadjusted=true&apiKey=uYgWTptpQgbpghz5Kvap0x9ElJG3O8Pq


    # https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=BSE%3APAISALO&apikey=ZT190HZDN99BS851
