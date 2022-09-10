from django.db import models


# Create your models here
class Prices(models.Model):
    order = models.CharField('Заказ №', max_length=20)
    price_usa = models.IntegerField('Стоимость, $')
    deliver_date = models.CharField('Дата поставки', max_length=30)
    price_rus = models.FloatField('Стоимость, Р')

    @property
    def get_price_rus(self, course):
        return round(self.price_usa * course, 2)

    def __str__(self):
        return self.order

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
