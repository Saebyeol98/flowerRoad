from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.urls import path, include

def index(request):
    return HttpResponse("하이")
def jsonSend(request):
    return JsonResponse({''})