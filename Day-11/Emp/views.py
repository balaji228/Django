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

def register(re):
	if re.method=="POST":
		na=re.POST['n']
		el=re.POST['em']
		ps=re.POST['p']
		ae=re.POST['a']
		d={'un':na,'eml':el,'pwd':ps,'age':ae}
		return render(re,'html/details.html',d)
	return render(re,'html/register.html')
