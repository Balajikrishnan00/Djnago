from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def GoodMorning(request):
    return HttpResponse('<h1>Good Morning!</h1>')
def GoodEvening(request):
    return HttpResponse('<h1>Good Evening</h1>')
def GoodNight(request):
    return HttpResponse('<h1>Good Night</h1>')
