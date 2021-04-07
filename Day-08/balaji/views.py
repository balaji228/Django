from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("<h2 style='background-color:black;color:blue;text-align:center'>Welcome to Home Page</h2>")

def chk(request):
	return HttpResponse("<script>alert('click OK 2 continue')</script><h2 style='background-color:black;color:blue;text-align:center'>BBB</h2>")
def home(request):
	return render(request,'bg/home.html')
def login(request):
	return render(request,'bg/login.html')
def reg(ch):
	return render(ch,'bg/register.html')