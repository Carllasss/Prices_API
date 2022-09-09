# from course import get_course
# from table import get_table
# from ..models import Prices
#
# class JOB()
#     RUN_EVERY_MINS = 1
#
#     shedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'webexample.my_cron_job'
#
#     def do(self):
#         course = get_course()
#         table = get_table('1hmTUTWuEnhoO5VmZLjT-kHN2dbPuIV5ij2Nx6j7K-hI')
#         for i in table:
#             new_price = Prices(order=i[1], price_usa=i[2], price_rus=(int(i[2]) * course), deliver_date=i[3])
#             new_price.save()