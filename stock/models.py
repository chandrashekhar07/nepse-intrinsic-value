from django.db import models

# Create your models here.

class StockModel (models.Model):
    symbol = models.CharField("Symbol",max_length=10,unique=True,null=False,blank=False)
    price = models.FloatField("Price",default=0)
    date =models.CharField("Date",default="1996-01-01",max_length=15)
    category =models.CharField("Category",max_length=25,default=" ")
    profit = models.FloatField("Profit",default=0)
    shares_outstanding= models.IntegerField("Shares_Outstanding",default=0)
    book_value = models.FloatField("Book_Value",default=0)

    def __str__(self):
        return self.symbol