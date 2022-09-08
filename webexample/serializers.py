from djangoProject import settings
from .models import Prices


def serializer_prices(prices):
    return [
        {'id': prices.id, 'order': prices.order, 'price_usa': prices.price_usa,
         'price_rus': prices.price_rus, 'delivery_date': prices.deliver_date}
    ]
