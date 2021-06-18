from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def hi(r):
    return HttpResponse('Welcome To Django')

def display(r):
    date=datetime.datetime.now()

    dict_date={'date':date,'name':'Balaji Krishnan','salary':32000}
    return render(r,'TempApp/01_TempApp.html',context=dict_date)

def TimeTable(r):
    return render(r,'TempApp/timeTable.html')

def WelcomePort(r):

    dateTime=datetime.datetime.now()
    hour=int(dateTime.strftime('%H'))
    name='Balaji'
    if hour<12:
        Greeting='Hi Good Morning'
    else:
        Greeting='hi Good Afternoon'
    greets={'time':dateTime,'greet':Greeting,'user':name}

    return render(r,'TempApp/welcomeport.html',context=greets)
def img(r):
    pass