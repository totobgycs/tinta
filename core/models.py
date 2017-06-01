from django.db import models

class Operation(models.Model):
    name = models.CharField(max_length=200)
    currency = models.CharField(blank=True, null=True, max_length=300, default='EUR')
    # value = volume * price
    value = models.FloatField(blank=True, null=True)
    position = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    valuation_date = models.DateField(blank=True, null=True)
    # the buys - the sells ... what about the expires?
    invested = models.FloatField(blank=True, null=True)
    # the ticker symbol (from yahoo finance) 
    underlying = models.CharField(blank=True, null=True,max_length=10)
    # operation start date (first trade), and end date (manual set, when pos is 0)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    def __str__(self):
        return 'Operation: '+self.name

class MarketData(models.Model):
    # the ticker symbol (from yahoo finance) 
    symbol = models.CharField(blank=True, null=True,max_length=10)
    price = models.FloatField(blank=True, null=True)
    poll_time = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return 'Market data: '+self.symbol


