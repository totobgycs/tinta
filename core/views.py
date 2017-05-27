from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Operation

from yahoo_finance import Share

def index(request):
    template = loader.get_template('core/dashboard.html')
    operations = [
        {'name': op.name, 'details': 'blah'} for op in Operation.objects.all()
    ]
    symbols = [
      'GOOG',
      'AAPL',
      'FB',
      'GE',
      '^ESX',
      '^AEX',
      '^GSPC',
      'ISP.MI',
      'ASML',
      'RDSB.L',
      'GBPEUR=X',
      'EURUSD=X',
    ]
    shares = [Share(sb) for sb in symbols]
    prices = [{'symbol': s.symbol, 'current_value': s.get_price()} for s in shares]

    context = {'operations': operations, 'shares': prices}
    return HttpResponse(template.render(context, request))

def operation(request, operation_id):
    try:
        operation = Operation.objects.get(pk=operation_id)
    except Question.DoesNotExist:
        raise Http404("Operation lookup failed.")
    template = loader.get_template('core/operation.html')
    context = {'operation': operation}
    return HttpResponse(template.render(context, request))
