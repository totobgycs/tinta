from functools import reduce

from yahoo_finance import Share

from .models import *


'''
Evaluate operation and retun metrics

Reads trades
Writes operation (some fileds)
Return some on-the-fly metrics
'''
def operation_metrics(operation):
    trades = operation.trade_set.order_by('trade_date')
    buys = trades.filter(openorclose = 'OP')
    sells = trades.filter(openorclose = 'CL')

    # calculate cumulative position and last 0-pos index, etc
    curr_pos = 0
    curr_exposure = 0
    max_exposure = 0
    flat_index = -1;
    for i, trade in enumerate(trades):
        curr_pos += trade.volume
        curr_exposure += trade.value
        if curr_pos == 0:
            flat_index = i
        if curr_exposure > max_exposure:
            max_exposure = curr_exposure
         
    value_buys = reduce(lambda x, y: x+y, [t.value for t in buys], 0)
    value_sells = reduce(lambda x, y: x+y, [t.value for t in sells], 0)
   
    # open position 
    open_pos = reduce(lambda x, y: x+y, [t.volume for t in trades], 0)
    
    # realized profits (only till the last closed positions)
    realized_profit = - reduce(lambda x, y: x+y, [t.value for t in trades[0:flat_index+1]], 0)

    # exposure (only from the last closed position)
    open_exposure = reduce(lambda x, y: x+y, [t.value for t in trades[flat_index+1:]], 0)

    # update the operation
    operation.realized_profit = realized_profit
    operation.exposure_value = open_exposure
    operation.position = open_pos
    operation.save()

    context = {
        'open_position': open_pos,
        'open_exposure': open_exposure,
        'max_exposure': max_exposure,
        'value_buys': value_buys,
        'value_sells': value_sells,
        'realized_profit': realized_profit,
    }

    return context
    
