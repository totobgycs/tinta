from django.db import models

CURRENCY_CHOICES = (
    # ('Code', 'Human-friendly label')
    ('EUR', 'Eur'),
    ('USD', 'Usd'),
    ('GBP', 'Gbp'),
)

OPENORCLOSE_CHOICES = (
    # ('Code', 'Human-friendly label')
    ('OP', 'Open'),
    ('CL', 'Close'),
)

class Operation(models.Model):
    name = models.CharField(max_length=200)
    # currency of the operation, by default: EUR
    currency = models.CharField(
        blank=True, null=True, max_length=3,
        default='EUR',
        choices=CURRENCY_CHOICES)
    is_active = models.BooleanField(default=True)
    # Open exposure (money currently at risk)
    exposure = models.FloatField(blank=True, null=True)
    # Open position
    position = models.FloatField(blank=True, null=True)
    # Profit (realized, at last flat position)
    realized_profit = models.FloatField(blank=True, null=True)
    
    # TODO: redo this model (some fileds belong to trades)
    # value = volume * price
    value = models.FloatField(blank=True, null=True)
    # 
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


class Trade(models.Model):
    # trade date
    trade_date = models.DateField(blank=True, null=True)
    # currency of the trade
    currency = models.CharField(
        blank=True, null=True, max_length=3,
        default='EUR',
        choices=CURRENCY_CHOICES)
    # how much money did we pay/get in this trade
    value = models.FloatField(
        blank=True, null=True,
        help_text="How much money did we pay in this trade (+ if we payed, - if we got the money)")
    # was this opening or closing a position
    openorclose = models.CharField(
        blank=True, null=True, max_length=2,
        default='OP',
        choices=OPENORCLOSE_CHOICES,
        help_text="Position opening or position closing")
    # instrument: what did we buy/sell
    instrument = models.CharField(blank=True, null=True, max_length=100)
    # the ticker symbol (from yahoo finance) 
    underlying = models.CharField(blank=True, null=True, max_length=10)
    # how many unit
    volume = models.FloatField(
        blank=True, null=True,
        help_text="Usually integer number of units (+ if we bought, - if we sold)")
    # unit price
    price = models.FloatField(blank=True, null=True)
    operation = models.ForeignKey(Operation, blank=True, null=True)
    def __str__(self):
        return "Trade: [{3}] {0} {1} for {4} {2}".format(
            self.value, self.currency, self.instrument, self.trade_date,
            self.volume)

    class Meta:
        ordering = ['trade_date']


