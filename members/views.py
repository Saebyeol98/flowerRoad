from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.urls import path, include
from .models import User


def setData(request):
    req_code = request.GET.get("req_code")
    if req_code is not None:
        if req_code == "find":
            try:
                userid = request.GET.get("userid")
                print(userid)
                data = User.objects.get(userid=userid)
            except Exception as err:
                return HttpResponse(str(err))  # 중복 아이디가 없으므로 사용가능
            return HttpResponse("Fail")  # 중복 아이디가 있습니다
        elif req_code == "login":
            try:
                userid = request.GET.get("userid")
                userpw = request.GET.get("userpw")
                data = User.objects.get(userid=userid, userpw=userpw)
            except Exception:
                return HttpResponse("Fail")
            return HttpResponse("Success")
        elif req_code == "user_create":
            try:
                userid = request.GET.get("userid")
                userpw = request.GET.get("userpw")
                phone = request.GET.get("phone")
                phone = changeNum(phone)
                birth_date = request.GET.get("date")
                birth_date = changeBirth(birth_date)
                addr = request.GET.get("addr")
                gender = request.GET.get("gend")
                email = request.GET.get("email")
                if email is None:
                    addData = User(userid=userid, userpw=userpw, phone_num=phone, birth_date=birth_date, addr=addr,
                                   gender=gender)   
                else:
                    addData = User(userid=userid, userpw=userpw, phone_num=phone, birth_date=birth_date, addr=addr,
                                   gender=gender, email=email)
                addData.save()
            except Exception:
                return HttpResponse("Fail")
            return HttpResponse("Success")
    else:
        return HttpResponse("해당하는 REQ_CODE가 없거나 누락되어있습니다...")
    return HttpResponse("Hello Django~!")


def changeNum(phone):
    front = phone[0:3]
    mid = phone[3:7]
    end = phone[7:]

    phone = front + '-' + mid + '-' + end
    return phone


def changeBirth(birth_date):
    year = birth_date[:4]
    month = birth_date[4:6]
    day = birth_date[6:]

    birth_date = year + '-' + month + '-' + day
    return birth_date

    
# 향후 구현예정 회원가입 후 이메일 인증 구현 SMTP
def man(request):
    return render(request, "members/mem_manager.html", {})


def login(request):
    return render(request, "members/login.html", {})


def register(request):
    return render(request, "members/userlog.html", {})

    
def mini(request):
    return render(request, "members/mini.html", {})


def pot(request):
    return render(request, "members/pot.html", {})


def main(request):
    return render(request, "members/main.html", {})

def diorama(request):
    return render(request, "members/diorama.html", {})


