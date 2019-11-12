from django.urls import path, include
from . import views # .은 현재위치다
from . views import genderAjax, BoardDataView
from django.conf.urls import url


urlpatterns = [
    path('', views.setData, name='setData'),
    path('select',views.selectBoard,name='select'),
    url(r'ajax/board_date/(?P<pk>[\w-]+)/$', genderAjax, name='board_date'),
    url(r'lone/$', BoardDataView, name='lone-list'),   
]