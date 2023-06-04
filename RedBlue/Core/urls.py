from django.urls import path, include

from Core.views import *

urlpatterns = [
    path('', index, name="index"),
    path('time/', get_time, name="time")
]