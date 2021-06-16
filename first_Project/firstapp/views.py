from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wish(request):
    mgs='''<head><title>Django firstApp</title>
    <body> <h1> Welcome Django</h1>
    </body></head>'''
    return HttpResponse(mgs)
