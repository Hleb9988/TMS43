from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path


from tasks.lesson03 import task303
from tasks.lesson03 import task310
from tasks.lesson03 import task311
from tasks.lesson04 import task402

def xxxx(req: HttpRequest) -> HttpResponse:
    return HttpResponse(
        f"Hello world! Metod {req.method}"
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", xxxx),
    path('tasks/303', task303.handler),
    path('tasks/310', task310.handler),
    path('tasks/311', task311.handler),
    path('tasks/402', task402.handler),
    path('api/v1/tasks/402/', task402.handler_api),
]
