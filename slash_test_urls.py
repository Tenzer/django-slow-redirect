from django.http import HttpResponse
from django.urls import path


def view(request):
    return HttpResponse("ok")


urlpatterns = [path("url/", view)]
