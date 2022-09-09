from celery import shared_task
from celery.utils.log import get_task_logger
from webexample.utils.course import get_course
from webexample.utils.table import get_table
from webexample.models import Prices

logger = get_task_logger(__name__)

@shared_task()
def mytask():
        course = get_course()
        table = get_table('1hmTUTWuEnhoO5VmZLjT-kHN2dbPuIV5ij2Nx6j7K-hI')
        for i in table:
            new_price = Prices(order=i[1], price_usa=i[2], price_rus=(int(i[2]) * course), deliver_date=i[3])
            new_price.save()
        print('done')
        logger.info("Task comleted")