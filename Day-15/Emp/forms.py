from Emp.models import UsrRg,NewData
from django import forms

class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','password']
		widgets={"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter username","required":True}),
		"password":forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter password","required":True}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email id","required":True})}

class Userupdate(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','age']
		widgets={
		"username":forms.TextInput(attrs={"class":"form-control","placeholder":"Update username","required":True}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"Update Email id","required":True}),
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Email id","required":True}),
		}

class NewUsrForm(forms.ModelForm):
	class Meta:
		model=NewData
		fields=['mobile','gender']
		widgets={"mobile":forms.NumberInput(attrs={"class":"form-control","placeholder":"Update Mobile Number","max":10}),
		"gender":forms.Select(attrs={"class":"form-control"}),
		}