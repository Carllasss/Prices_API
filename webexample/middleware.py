import http.client
import os
import environ
from django.http import HttpRequest, HttpResponse
from django.urls import reverse

from djangoProject import settings


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        if request.path.startswith('/admin/'):
            return response
        x_key = request.headers.get("X-API-KEY")
        key = settings.API_KEY
        if x_key != key:
            return HttpResponse(status=403)
        print(request)

        return response
