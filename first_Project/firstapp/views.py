from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wish(request):
    mgs='<h1> welcome to Django in my first project.</h1>'
    return HttpResponse(mgs)
