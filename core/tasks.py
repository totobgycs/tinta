from __future__ import absolute_import, unicode_literals

from datetime import datetime

from celery import shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from celery.utils.log import get_task_logger

from yahoo_finance import Share

from .models import MarketData

logger = get_task_logger(__name__)
 
@periodic_task(run_every=(crontab(hour="*", minute="*", day_of_week="*")))
def poll_market_data():
    logger.info("Start task")
    now = datetime.now()
    mds = MarketData.objects.all()
    for md in mds:
        yahoo_share = Share(md.symbol)
        md.price = yahoo_share.get_price()
        md.poll_time = now
        md.save()

    logger.info("Task finished")

