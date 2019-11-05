from django.urls import path, include

from . import views # .은 현재위치다.

urlpatterns = [
    path('', views.index, name='index'),
    path('userid=<userid>&userpw=<userpw>&phone=<phone>&date=<date>&addr=<addr>&gend=<gend>', views.addUser, name='addUser'),
    path('userid=<userid>&userpw=<userpw>', views.login, name='login'),
    path('userid=<userid>', views.checkUser, name='check')
    # path('', views.index, name='index'),
    # path('go', views.start, name='start'),
    # path('go=<text>', views.third, name='third'),
    # path('name=<name>&age=<age>', views.profile, name='profile')
]