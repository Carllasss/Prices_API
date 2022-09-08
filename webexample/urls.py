
from django.urls import path

from .views import PricesListView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('prices', PricesListView.as_view(), name='prices')
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)