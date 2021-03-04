from django.urls import path

from .views import handler
from .views import handler_api

urlpatterns = [
    path("", handler),
    path("api/", handler_api),
]