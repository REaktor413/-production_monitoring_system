from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
import json

from .models import *


def index(request):
    careers = Careers.objects.all()
    samples = Samples.objects.filter(production_date__gte= (str(datetime.now().year-1)+"-01-01"))

    update_mined = [0 for x in range(len(careers))]
    for item in Samples.objects.all():
        for career in careers:
            if career.title == item.career:
                update_mined[career.pk-1] += item.production_tonnage

    for mined in update_mined:
        career = Careers.objects.filter(pk=update_mined.index(mined)+1)
        career.update(mined=mined)
        rest = ((career[0].reserves - mined) / career[0].reserves) * 100
        career.update(residue=rest)


    data_years = [[0 for x in range(12)] for y in range(len(careers))]
    for item in samples:
        for career in careers:
            if career.title == item.career:
                data_years[career.pk-1][item.production_date.month-1] += item.production_tonnage

    data_years = json.dumps(data_years)
    context = {
        'careers': careers,
        'title': 'Главная страница',
        'name': 'Карьеры',
        'user': 'USER',
        "data_years": data_years,
        }

    return render(request, 'SMA/index.html', context=context)

def calendar(request):
    careers = Careers.objects.all()
    return render(request, 'SMA/app-event-calender.html', {'careers': careers, 'title': 'Главная страница'})
