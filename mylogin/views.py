from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, BlogAdd,ForgetPasswordForm,ResendForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from myapp.models import Blog
import datetime
from django.core.mail import EmailMessage
from django.core.exceptions import ValidationError
import base64
import binascii
# Create your views here.
def get_name(request):
    if (request.user.is_authenticated()):
        return redirect('/blog/blogs/')
    if (request.method == 'GET'):
        form = LoginForm()
        next_url = request.GET.get('next', '')
        return render(request, 'mylogin/name.html', {'form' : form ,'next': next_url})
        #return render(request, 'mylogin/name.html', {'form': form})
    if (request.method == 'POST'):
        next_url = request.POST.get('next', '')
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            passwd = form.cleaned_data['password']
            user = authenticate(username=uname, password=passwd)
            if user is not None :
                a=User.objects.get(username=uname)
                if a.is_active==False :
                    #return HttpResponse("Confirm the Registration link !!")
                    body="Confirm the Registration by clicking on the Link sent to your Email Id"
                    return render(request, 'mylogin/message.html', {'message': body})
                login(request, user)
                print(next_url)
                if next_url :
                    return redirect(next_url)
                return redirect('/blog/blogs/')
            # print (user.get_full_name())
            else:
                #return HttpResponse("Invalid User")
                body="Invalid User !! Either You have not registered on your website or you entering wrong username or password !! "
                return render(request, 'mylogin/message.html', {'message': body})
        else:
            return render(request, 'mylogin/name.html', {'form': form})


def log_out(request):
    logout(request)
    #html = r'''<html> <head> <title> Log Out </title> </head> <body> <center>  You have Logout Successfully !! Hope to see you again !!  </center> <hr> <a href="http://127.0.0.1:8000/blog/"> Click Here to log in again !! </a> </body> </html>'''
    body="You Have Logout Successfully !! "
    return render(request, 'mylogin/message.html', {'message': body})
    #return HttpResponse(html)


def sign_up(request):
    if (request.user.is_authenticated()):
        return redirect('/blog/blogs/')
    form = SignupForm()
    return render(request, 'mylogin/signup.html', {'form': form})


def add_blog(request):
    if not request.user.is_authenticated():
        return redirect('/get_name/')
    form = BlogAdd()
    return render(request, 'mylogin/blogadd.html', {'form': form})


def add_user(request):
    print(request)
    if (request.method == 'POST'):
        form = SignupForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            pwd=form.cleaned_data['password']
            email_id=form.cleaned_data['email']
            firstname=form.cleaned_data['first_name']
            lastname=form.cleaned_data['last_name']
            pwd1=form.cleaned_data['password1']
            if pwd1 != pwd:
                #raise ValidationError("Passwords Didnot match ")
                body="Passwords Didnot Match !! Try Again"
                return render(request, 'mylogin/message.html', {'message': body})
            list=User.objects.all()
            for item in list:
                if uname==item.username:
                    #return HttpResponse("A user exists there with the same Username ")
                    body="A User exists with the same Username !! Try again with a different Username "
                    return render(request, 'mylogin/message.html', {'message': body})
            subject='Complete your registration'
            token=uname.encode()
            token=base64.b64encode(token)
            #token=uname
            message="Hi %s click on the following link to confirm your registration. The Link is :http://127.0.0.1:8000/blog/activate/%s " %(uname,token)
            email=EmailMessage(subject,message,to=[email_id])
            email.send()
            a=User.objects.create_user(username=uname,password=pwd,first_name=firstname,last_name=lastname,email=email_id)
            a.is_active=False
            a.save()
            #return HttpResponse("An email has been sent to ur email id !")
            body="An email has been sent to ur email id ! Click on that link to complete your registration !! "
            return render(request, 'mylogin/message.html', {'message': body})
        #print(form.errors.as_data())
        #return HttpResponse(form.errors.as_data())
        return render(request, 'mylogin/signup.html', {'form': form})
    #html = r'''<html> <head> <title> Blog Is Not valid !! </title> </head> <body > <center> Blog Is Not valid!! Type all the required fields !! </center><hr> <a href="http://127.0.0.1:8000/blog/addblog/"> Click here to Create blog  Again !! </a> </body> </html>'''
    #return HttpResponse(html)
    body="Invalid Details !! Try again !!  "
    return render(request, 'mylogin/message.html', {'message': body})

def authenticate_user(request):
    a=request.get_full_path()
    #print(a)
    #return HttpResponse(a)
    if "activate/b'" not in a:
        body="404 Page Not Found !!"
        return render(request,'mylogin/message.html',{'message':body})

    name=a.split("'")[-1]
    name=name.encode()
    #name=name+"'"
    #print(name)
    #return HttpResponse(name)
    try:
        name=base64.b64decode(name)
    except binascii.Error:
        body="404 Page Not Found !!"
        return render(request,'mylogin/message.html',{'message':body})

    #return HttpResponse(name)
    name=name.decode()
    #print(name)
    flag=False
    list=User.objects.all()
    for item in list:
        if name==item.username:
            flag=True
            break
    if flag==False:
        body="404 Page Not Found !!"
        return render(request,'mylogin/message.html',{'message':body})
    obj=User.objects.get(username=name)
    if obj.is_active==True:
        #return HttpResponse("You Have already registered !!")
        body="Dear %s , You have already registered ! Kindly Log In !! " %(obj.username)
        return render(request, 'mylogin/message.html', {'message': body})
    obj.is_active=True
    #obj.is_staff=True
    #obj.is_superuser=True
    obj.save()
    body="Dear %s, You Have successfully completed your registration on our website !! You can now Log In, Create Blogs and Comment on other Blogs" %(obj.username)
    return render(request,'mylogin/message.html',{'message':body})
    #return HttpResponse(obj.username)


def publish_blog(request):
    print(request)
    if (request.method == 'POST'):
        form = BlogAdd(request.POST)
        if form.is_valid():
            heading = form.cleaned_data['title']
            content = form.cleaned_data['body']
            a = Blog.objects.create(title=heading, body=content, pub_date=datetime.datetime.now())
            html = r'''<html> <head> <title> Blog created successfully !! </title> </head> <body > <center> Blog has been created Successfully !! </center><hr> <a href="http://127.0.0.1:8000/blog/blogs"> Click here to view the blogs !! </a> </body> </html>'''
            return HttpResponse(html)

    html = r'''<html> <head> <title> Blog Is Not valid !! </title> </head> <body > <center> Blog Is Not valid!! Type all the required fields !! </center><hr> <a href="http://127.0.0.1:8000/blog/addblog/"> Click here to Create blog  Again !! </a> </body> </html>'''
    return HttpResponse(html)
	

def get_username(request):
    if (request.user.is_authenticated()):
        return redirect('/blog/blogs/')
    if (request.method == 'POST'):
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            flag=False
            list=User.objects.all()
            for item in list:
                if uname==item.username:
                    flag=True
                    break
            if flag==False:
                body="You have entered an invalid username. !! Kindly enter the Correct Username !! "
                return render(request,'mylogin/message.html',{'message':body})
            a=User.objects.get(username=uname)
            name=uname.encode()
            new_pwd=base64.b64encode(name)
            new_pwd=new_pwd.decode()
            a.set_password(new_pwd)
            subject="Your New Password"
            message="Hi %s This is your new password %s " %(uname,new_pwd)
            email=EmailMessage(subject,message,to=[a.email])
            email.send()
            a.save()
            #html = r'''<html> <head> <title> Password sent successfully !! </title> </head> <body > <center> Password has been sent Successfully  to your registered enail id !! !! </center><hr> </body> </html>'''
            #return HttpResponse(html)
            body="Password has been sent Successfully  to your registered email id !! !! "
            return render(request, 'mylogin/message.html', {'message': body})
        else:
            #body="Enter the Correct Username !! "
            return render(request,'mylogin/forgetpwd.html',{'form':form})
    #html = r'''<html> <head> <title> Blog Is Not valid !! </title> </head> <body > <center> Blog Is Not valid!! Type all the required fields !! </center><hr> <a href="http://127.0.0.1:8000/blog/addblog/"> Click here to Create blog  Again !! </a> </body> </html>'''
    #return HttpResponse(html)
    else:
        form = ForgetPasswordForm()
        return render(request, 'mylogin/forgetpwd.html', {'form': form})


def resend_link(request):
    if (request.user.is_authenticated()):
        return redirect('/blog/blogs/')
    if (request.method == 'POST'):
        form = ResendForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            flag=False
            list=User.objects.all()
            for item in list:
                if uname==item.username:
                    flag=True
                    break
            if flag==False:
                body="You have entered an invalid username. !! Kindly enter the Correct Username !! "
                return render(request,'mylogin/message.html',{'message':body})
            a=User.objects.get(username=uname)
            subject='Complete your registration'
            token=uname.encode()
            token=base64.b64encode(token)
            #token=uname
            email_id=a.email
            message="Hi %s click on the following link to confirm your registration. The Link is :http://127.0.0.1:8000/blog/activate/%s " %(uname,token)
            email=EmailMessage(subject,message,to=[email_id])
            email.send()
            #a=User.objects.create_user(username=uname,password=pwd,first_name=firstname,last_name=lastname,email=email_id)
            a.is_active=False
            a.save()
            #return HttpResponse("An email has been sent to ur email id !")
            body="An email has been Re-sent to ur email id ! Click on that link to complete your registration !! "
            return render(request, 'mylogin/message.html', {'message': body})
        else:
            #body="Enter the Correct Username !! "
            return render(request,'mylogin/resend.html',{'form':form})
    #html = r'''<html> <head> <title> Blog Is Not valid !! </title> </head> <body > <center> Blog Is Not valid!! Type all the required fields !! </center><hr> <a href="http://127.0.0.1:8000/blog/addblog/"> Click here to Create blog  Again !! </a> </body> </html>'''
    #return HttpResponse(html)
    else:
        form = ResendForm()
        return render(request, 'mylogin/resend.html', {'form': form})
