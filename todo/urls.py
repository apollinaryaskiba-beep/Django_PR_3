from django.urls import path
from django.http import HttpResponse

# Проверка
def index(request):
    return HttpResponse("Приложение Todo работает!")

urlpatterns = [
    path('', index, name='index'),
]