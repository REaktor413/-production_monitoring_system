from django.urls import path
from .views import *


urlpatterns = [
     path('', index),
     path('index.html', index),
     path('app-event-calender.html', calendar),

     ]