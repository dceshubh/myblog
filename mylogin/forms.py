from django import forms
from django.contrib.auth.models import User
from myapp.models import Blog

class SignupForm(forms.Form):
	username=forms.CharField(label="Username",max_length=20,required=True)
	email=forms.EmailField(label="Email Id ", required=True)
	first_name=forms.CharField(label="First Name",required=False)
	last_name=forms.CharField(label="Last Name",required=False)
	password = forms.CharField(label="Password",max_length=32, required=True,widget=forms.PasswordInput)
	password1=forms.CharField(label="Password(again)",max_length=32,required=True,widget=forms.PasswordInput)
	
	#class Meta:
		#model=User
		#fields=['username','email','password','first_name','last_name']
		
class LoginForm(forms.Form):
	username=forms.CharField(initial="", required=True)
	#password=forms.CharField(initial="",required=True)
	password = forms.CharField(initial="",max_length=32, required=True,widget=forms.PasswordInput)

class BlogAdd(forms.Form):
	title=forms.CharField(label='Enter the Title of your blog ',max_length=100,required=True)
	#pub_date=forms.DateTimeField(label='date published')
	body=forms.CharField(label='Enter the body of your blog',widget=forms.Textarea,required=True)
	#class Meta:
		#model=Blog
		#fields=['title','pub_date','body']

class ForgetPasswordForm(forms.Form):
    username=forms.CharField(initial="",required=True)

class ResendForm(forms.Form):
    username=forms.CharField(initial="",required=True)
