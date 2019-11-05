from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 
from django.urls import path, include
from .models import User

def index(request):
    return HttpResponse("하이")

def addUser(request,userid, userpw, phone, date, addr, gend):
    userid = str(userid)
    userpw = str(userpw)
    phone = '010-1234-5678'
    date = '1997-10-12'
    addr = str(addr)
    gend = str(gend)
    data = User(userid=userid,userpw=userpw,phone_num=phone,birth_date=date,addr=addr,gender=gend)
    data.save()
    return HttpResponse("회원가입 완료")

def checkUser(request, userid):
    try:
        data = User.objects.get(userid=str(userid))
        data2 = User.objects.all()
    except:
        return HttpResponse("Success")
    return HttpResponse("Fail")

def login(request, userid, userpw):
    try:
        data = User.objects.get(userid=str(userid),userpw=str(userpw))
    except Exception:
        return HttpResponse("Fail")
    return HttpResponse("Success")
