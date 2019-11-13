from django.urls import path, include

from . import views # .은 현재위치다.

app_name = "members"

urlpatterns = [
    path('', views.setData, name='setData'),
    path('man', views.man, name='man'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('mini', views.mini, name='mini'),
    path('pot', views.pot, name='pot'),
    path('main', views.main, name='main'),
    path('diorama', views.diorama, name='diorama'),
    #path('userid=<userid>&userpw=<userpw>&phone=<phone>&date=<date>&addr=<addr>&gend=<gend>', views.addUser, name='addUser')
    #path('userid=<userid>&userpw=<userpw>', views.login, name='login'),
    #path('userid=<userid>', views.checkUser, name='check')

]