from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def reg(request):
    return render(request,'reg.html')

