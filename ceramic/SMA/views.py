from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    careers = Careers.objects.all()
    context = {
        'careers': careers,
        'title': 'Главная страница',
        'name': 'Карьеры',
        'user': 'USER'
            }
    return render(request, 'SMA/index.html', context=context)

def calendar(request):
    careers = Careers.objects.all()
    return render(request, 'SMA/app-event-calender.html', {'careers': careers, 'title': 'Главная страница'})
