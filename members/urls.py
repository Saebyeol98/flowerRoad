from django.urls import path, include

from . import views # .은 현재위치다.

urlpatterns = [
    path('', views.setData, name='setData'),
    path('useradd', views.useradd, name='useradd'),
    #path('userid=<userid>&userpw=<userpw>&phone=<phone>&date=<date>&addr=<addr>&gend=<gend>', views.addUser, name='addUser')
    #path('userid=<userid>&userpw=<userpw>', views.login, name='login'),
    #path('userid=<userid>', views.checkUser, name='check')

]