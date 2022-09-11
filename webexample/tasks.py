from pathlib import Path

from celery import shared_task
from celery.utils.log import get_task_logger
from webexample.clients.rate import get_course
from webexample.clients.google_sheet import get_table, get_id_list
import environ
import os

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
logger = get_task_logger(__name__)

@shared_task()
def update_table():
    from webexample.models import Prices
    course = get_course()
    table = get_table(os.environ.get('SERVICE_KEY'))
    for line in table:
        try:
            new_price = Prices.objects.get(order=line[1])
            if new_price.price_usa != line[2] or new_price.price_rus != (int(line[2]) * course) or new_price.deliver_date != line[3]:
                new_price.price_rus = (int(line[2]) * course)
                new_price.price_usa = line[2]
                new_price.deliver_date = line[3]
                new_price.save()
        except Prices.DoesNotExist:
            new_price = Prices(order=line[1], price_usa=line[2], price_rus=(int(line[2]) * course), deliver_date=line[3])
            new_price.save()

        prices = Prices.objects.all()
        for line in prices:
            if line.order not in get_id_list(table):
                delete_price = Prices.objects.filter(order=line.order)
                delete_price.delete()

    logger.info("Task comleted")
