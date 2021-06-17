from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def function1(request):
    return HttpResponse('<h2> welcome to f1</h2>')

def function2(request):
    return HttpResponse( '<h2> welcome to f2</h2>')

def function3(request):
    return HttpResponse ('<h2> welcome to f3</h2>')

def telTime(r):
    time= datetime.datetime.now()
    return HttpResponse(time)