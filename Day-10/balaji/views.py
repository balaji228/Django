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
	if ch.method=="POST":
		emailaddress=ch.POST['a']
		pasword=ch.POST['b']
		ag=ch.POST['age']
		return render(ch,'bg/home.html',{'info':emailaddress,'info1':pasword})
	return render(ch,'bg/register.html')
def bthm(re):
	return render(re,'bg/bthm.html')
def about(ra):
	return render(ra,'bg/about.html')
def contact(ca):
	return render(ca,'bg/contact.html')