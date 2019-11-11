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
                data = User.objects.get(userid=userid)
            except Exception:
                return HttpResponse("Success")  # 중복 아이디가 없으므로 사용가능
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
                birth_date = request.GET.get("date")
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

# 향후 구현예정 전화번호 01012319900 > 010-1231-9900 메서드 구현

# 향후 구현예정 생년월일 19980101 > 1998-01-01 메서드 구현

# 향후 구현예정 회원가입 후 이메일 인증 구현 SMTP


def useradd(request):
    return render(request, "members/insert.html", {})