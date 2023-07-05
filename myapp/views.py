from django.http import HttpResponse
from django.shortcuts import render
import datetime

def home(request):
    
    # return HttpResponse("<h1>Hello Django</h1>")
    return render(request,"home.html", {})

