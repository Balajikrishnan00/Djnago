
from django.contrib import admin
from django.urls import path
from tempApp import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('hai/',views.hi),
    path('display/',views.display),
    path('timetable/',views.TimeTable),
    path('welcomePort/',views.WelcomePort),
]
