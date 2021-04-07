from django.shortcuts import render,redirect
from Emp.models import UsrRg
from Emp.forms import UsregForm
from django.http import HttpResponse
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
def crud(re):
	if re.method=="POST":
		na=re.POST['name']
		el=re.POST['eml']
		ps=re.POST['pwd']
		ae=re.POST['age']
		data2=UsrRg.objects.all()
		if len(na)!=0:
			data=UsrRg.objects.create(username=na,password=ps,email=el,age=ae)
			return render(re,'html/actions.html',{'info':data2})
	data2=UsrRg.objects.all()
	return render(re,'html/actions.html',{'info':data2})

def delt(re,id):
	data=UsrRg.objects.get(id=id)
	data.delete()
	return redirect('/cr')

def dform(re):
	if re.method=="POST":
		e = UsregForm(re.POST)
		if e.is_valid():
			e.save()
			return HttpResponse("User Created Successfully")
	e = UsregForm()
	return render(re,'html/dyform.html',{'tu':e})


