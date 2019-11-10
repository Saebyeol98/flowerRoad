from django.urls import path, include

from . import views # .은 현재위치다.

urlpatterns = [
    path('', views.setData, name='setData')
]