from django.shortcuts import render,redirect
from Emp.models import UsrRg,NewData
from Emp.forms import UsregForm,Userupdate,NewUsrForm
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
			q=e.save()
			y=NewData.objects.create(pid_id=q.id)
			return redirect('/sh')
	e = UsregForm()
	return render(re,'html/dyform.html',{'tu':e})

def show(re):
	data=UsrRg.objects.all()
	return render(re,'html/show.html',{'info':data})

def userdel(re,et):
	data=UsrRg.objects.get(id=et)
	if re.method=="POST":
		data.delete()
		return redirect('/sh')
	return render(re,'html/userdel.html',{'sd':data})

# def useredit(re,ei):
# 	data=UsrRg.objects.get(id=ei)
# 	if re.method=="POST":
# 		data.username=re.POST['username']
# 		data.email=re.POST['email']
# 		data.password=re.POST['password']
# 		data.age=re.POST['age']	
# 		data.save()
# 		return redirect('/sh')
# 	return render(re,'html/useredit.html',{'info':data})

def updateuser(rt,si):
	a=UsrRg.objects.get(id=si)
	y=NewData.objects.get(pid_id=si)
	if rt.method=="POST":
		d=Userupdate(rt.POST,instance=a)
		k=NewUsrForm(rt.POST,instance=y)
		if d.is_valid() and k.is_valid:
			d.save()
			k.save()
			return redirect('/sh')
	d=Userupdate(instance=a)
	k=NewUsrForm()
	return render(rt,'html/updateuser.html',{'us':d,'nt':k})

def userinfo(ty,uname):
	p=UsrRg.objects.get(username=uname)
	t=NewData.objects.get(pid_id=p.id)
	return render(ty,'html/uinfo.html',{'y':p,'yu':t})

