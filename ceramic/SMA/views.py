from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def index(request):
    careers = Careers.objects.all()
    return render(request, 'SMA/index.html', {'careers': careers, 'title': 'Главная страница'})
