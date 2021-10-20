from bs4 import BeautifulSoup
import requests
from stock.models import StockModel
from django.http import HttpResponse
from django.shortcuts import render

def getDetails(request):
    try:
        query = request.GET['q']
        if query:
            stocks = StockModel.objects.filter(category=query)
            for item in stocks:
                try:
                    url='https://nepsealpha.com/stocks/'+str(item)+'/info'
                    htmlText = requests.get(url).text
                    soup = BeautifulSoup(htmlText,'lxml')
                    tableInfo = soup.find_all('table',class_='table table-hover table-striped table-border')
                    priceInfo=tableInfo[0].thead.h2.text
                    priceListUnfiltered=priceInfo.split('\n')
                    priceListUnfiltered = [item.strip() for item in priceListUnfiltered if item ]
                    price = priceListUnfiltered[1]
                    print('Price is ',price)
                    symbol = priceListUnfiltered[0].split('\xa0')[0]
                    
                    # if symbol != item.symbol or symbol != item.symbol.upper():
                    #     print("not found",item.symbol)
                    #     continue

                    print('Symbol is',symbol)
                    date = priceListUnfiltered[0].split('\xa0')[1].split(':')[1].strip()[-13:]
                    print("Date is",date)
                    print('\n')
                    detils = tableInfo[0].tbody.text.split('\n')
                    detils = [item.strip() for item in detils if item.strip()]          
                

                    item.typee=priceListUnfiltered[0].split('\xa0')[1].split(':')[1][:-13].strip()

                    item.symbol = symbol
                    item.price = price
                    item.date = date
                 
                    item.save()
                except:
                    print("Error updating",item)
                finally:
                    print("")

            return render(request,'scheduler/index.html',{'text':query})
    except:        
        return render(request,'scheduler/index.html',{'text':"no querry found"})