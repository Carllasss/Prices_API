
from django.urls import path

from .views import PricesListView, get_info
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('prices', PricesListView.as_view(), name='prices'),
    path('list', get_info, name='get_info')
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)