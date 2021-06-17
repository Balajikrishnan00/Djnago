from django.urls import path
from TestApp import views

urlpatterns = [
    path('f1/',views.function1),
    path('f2/',views.function2),
    path('f3/',views.function3),
    path('time/',views.telTime),

]
