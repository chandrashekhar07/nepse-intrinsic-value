from django.db import models

# Create your models here.


class StockModel (models.Model):
    symbol = models.CharField("Symbol", max_length=10,
                              unique=True, null=False, blank=False)
    price = models.FloatField("Price", default=0)
    date = models.CharField("Date", default="1996-01-01", max_length=15)
    category = models.CharField("Category", max_length=25, default=" ")
    book_value = models.FloatField("Book_Value", default=0)
    eps = models.FloatField("Eps", default=0)
    roe = models.FloatField("Roe", default=0)
    year = models.CharField("year",default="", max_length=25)

    def __str__(self):
        return self.symbol
