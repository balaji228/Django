from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(re):
	return render(re,'html/about.html')

def contact(ra):
	return render(ra,'html/contact.html')

def login(re):
	return render(re,'html/login.html')