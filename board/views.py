from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.urls import path, include
from members.models import User
from .models import BoardData
from datetime import datetime


def setData(request):
    req_code = request.GET.get("req_code")
    if req_code is not None:
        if req_code == "board_write":
            board_title = request.GET.get("title")
            board_content = request.GET.get("content")
            userid = request.GET.get("userid")
            board_writer = User.objects.get(userid=userid)
            board_date = getNow()

            try:
                addData = BoardData(board_title=board_title, board_content=board_content, board_writer=board_writer,
                                    board_date=board_date)
                addData.save()
            except Exception as err:
                # return HttpResponse("Fail")
                return HttpResponse("오류가 발생했습니다!!!<br>" + str(err))
            return HttpResponse("Success")
    else:
        return HttpResponse("해당하는 REQ_CODE가 없거나 누락되어있습니다...")

    return HttpResponse("Hello Django~!")


def getNow():
    now = datetime.now()
    y_m_d = str(str(now.year) + "-" + str(now.month) + "-" + str(now.day))
    h_m_s = str(str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    date = str(y_m_d + " " + h_m_s)
    return date


def selectBoard(request) : 
    myresult =BoardData.objects.all()
    return HttpResponse(myresult[0].board_title +' ' +myresult[0].board_content +' ' +myresult[0].board_date)