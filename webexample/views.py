import json

import requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from .forms import PriceForm
from .models import Prices
from .serializers import serializer_prices


def get_info(request):
    """Gets lines from DB for HTML"""
    objs = Prices.objects.all()
    return render(request, 'base.html', {'objs': objs})


class PricesListView(View):
    """Basic model class with standard methods for API"""
    async def get(self, request):
        limit = int(request.GET.get('limit', 20))
        offset = int(request.GET.get('offset', 0))

        prices = await Prices.objects.all()[offset: offset + limit]

        return JsonResponse(dict(prices=serializer_prices(prices)))

    async def post(self, request):
        try:
            data = json.loads(request.body)

            form = PriceForm(data)
            if form.is_valid():
                order = form.cleaned_data.get('order')
                price_usa = form.cleaned_data.get('price_usa')
                price_rus = form.cleaned_data.get('price_rus')
                delivery_date = form.cleaned_data.get('delivery_date')
                new_price = Prices(order=order, price_usa=price_usa, price_rus=price_rus, deliver_date=delivery_date)
                await new_price.save()
                return HttpResponse('success')
        except (requests.exceptions.JSONDecodeError, TypeError, ValueError):
            return JsonResponse(dict(error='invalid JSON'), status=400)

        return HttpResponse('success2')

    async def delete(self, request, id):
        price = await Prices.objects.filter(id=id)
        if not price:
            return JsonResponse(dict(error='not price'), status=404)
        await price.delete()
        return HttpResponse(id)
