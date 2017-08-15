from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from functools import reduce

from yahoo_finance import Share

from .models import *
from .services import *

@login_required
def index(request):
    # the market
    mds = MarketData.objects.all()
    prices = [{'symbol': md.symbol, 'current_value': md.price} for md in mds]
    
    # our portfolio
    operations = Operation.objects.order_by('-exposure_value')

    profit = sum([op.realized_profit for op in operations])
    exposure = sum([op.exposure_value for op in operations])

    context = {
        'operations': operations,
        'shares': prices,
        'profit': profit,
        'exposure': exposure,
    }
    template = loader.get_template('core/dashboard.html')
    return HttpResponse(template.render(context, request))


@login_required
def operations(request):
    operations = Operation.objects.all()
    trades = Trade.objects.all()
    context = {}
    template = loader.get_template('core/operations.html')
    return HttpResponse(template.render(context, request))


@login_required
def operation(request, operation_id):
    try:
        operation = Operation.objects.get(pk=operation_id)
    except Question.DoesNotExist:
        raise Http404("Operation lookup failed.")

    trades = operation.trade_set.order_by('trade_date')
    buys = trades.filter(openorclose = 'OP')
    sells = trades.filter(openorclose = 'CL')

    # calculate cumulative position and last 0-pos index, etc
    cum_positions = [0] * len(trades)
    cum_invested = [0] * len(trades)
    curr_pos = 0
    curr_invested = 0
    for i, trade in enumerate(trades):
        curr_pos += trade.volume
        cum_positions[i] = curr_pos
        curr_invested += trade.value
        cum_invested[i] = curr_invested
         
    m = operation_metrics(operation)

    context = {
        'operation': operation,
        'trades': trades,
        'cum_positions': cum_positions,
        'cum_invested': cum_invested,
        'open_pos': m['open_position'],
        'open_exposure': m['open_exposure'],
        'value_buys': m['value_buys'],
        'value_sells': m['value_sells'],
        'realized_profit': m['realized_profit'],
    }
    template = loader.get_template('core/operation.html')
    return HttpResponse(template.render(context, request))
