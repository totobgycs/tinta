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
 
@periodic_task(run_every=(crontab(hour="*", minute="0,15,30,45", day_of_week="*")))
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


@periodic_task(run_every=(crontab(hour="*", minute="0,15,30,45", day_of_week="*")))
    logger.info("Start task: update operation")
    logger.info("Task finished: update operation")

