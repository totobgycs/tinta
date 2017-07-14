from __future__ import absolute_import, unicode_literals

from datetime import datetime

from celery import shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger

from yahoo_finance import Share

from .models import *
from .services import *

logger = get_task_logger(__name__)

@shared_task
def test_mul(x, y):
    return x * y
 
@periodic_task(run_every=(crontab(minute="*/2")))
def poll_market_data():
    logger.info("Start task: update market data")
    now = datetime.now()
    mds = MarketData.objects.all()
    for md in mds:
        yahoo_share = Share(md.symbol)
        price = yahoo_share.get_price()
        if price:
            md.price = price
            md.poll_time = now
            md.save()

    logger.info("Task finished: update market data")


@periodic_task(run_every=(crontab(minute="*/2")))
def update_operation():
    logger.info("Start task: update operation")
    operations = Operation.objects.all()
    for operation in operations:
        operation_metrics(operation)
    logger.info("Task finished: update operation")

