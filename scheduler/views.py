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
                    url='https://www.sharesansar.com/company/'+str(item)
                    htmlText = requests.get(url).text
                    soup = BeautifulSoup(htmlText,'lxml')
                    tableInfo = soup.find_all('div',class_="first-row margin-bottom-15")
                    data = tableInfo[0].text.strip().split('\n')
                    date= data[0].split(':')[1].strip()
                                   
                    item.price = data[1].replace(",","")
                    item.date = date
                 
                    item.save()
                    print(item.symbol,item.price)

                except Exception as e:
                    print("Error updating",item)
                    print(e)
                finally:
                    print("")

            return render(request,'scheduler/index.html',{'text':query})
        else:
            print("query not found")     


    except:   
        return render(request,'scheduler/index.html',{'text':"no querry found"})