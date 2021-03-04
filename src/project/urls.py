from django.contrib import admin
from django.urls import include
from django.urls import path

from project import views

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
    path("tasks/402/", include("applications.task402.urls")),
    path("tasks/310/", include("applications.task310.urls")),
    path("tasks/311/", include("applications.task311.urls")),
    path("tasks/303/", include("applications.task303.urls")),


]