from celery import shared_task
from celery.utils.log import get_task_logger
from webexample.utils.course import get_course
from webexample.utils.table import get_table, get_id_list


logger = get_task_logger(__name__)

@shared_task()
def mytask():
    from webexample.models import Prices
    course = get_course()
    table = get_table('1hmTUTWuEnhoO5VmZLjT-kHN2dbPuIV5ij2Nx6j7K-hI')
    for i in table:
        object = Prices.objects.filter(order=i[1])
        if object:
            object = Prices.objects.get(order=i[1])
            if object.price_usa != i[2] or object.price_rus != (int(i[2]) * course) or object.deliver_date != i[3]:
                object.price_rus = (int(i[2]) * course)
                object.price_usa = i[2]
                object.deliver_date = i[3]
                object.save()
        else:
            new_price = Prices(order=i[1], price_usa=i[2], price_rus=(int(i[2]) * course), deliver_date=i[3])
            new_price.save()

        prices = Prices.objects.all()
        for i in prices:
            if i.order not in get_id_list(table):
                delete_price = Prices.objects.filter(order=i.order)
                delete_price.delete()

    print('done')
    logger.info("Task comleted")
