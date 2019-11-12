from django.urls import path, include
from . import views # .은 현재위치다

app_name = "board"

urlpatterns = [
    path('', views.setData, name='setData'),
    path('select',views.selectBoard,name='select'),
    path('man', views.man, name='man'),
]