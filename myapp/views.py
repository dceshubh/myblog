from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime
from django.core import serializers
from myapp.models import Blog,Comments
from django.shortcuts import render,redirect

# Create your views here.

def firstpage(request):
	html=r'''<html> <head> <title> Shubham Varshney's Blog </title> </head> <body> <h1 align='center'> Welcome to My Blogs </h1> <a href="http://127.0.0.1:8000/blog/blogs/" > <h2 align='center'> My Blogs  </h2> </a> <a href="http://127.0.0.1:8000/blog/latest/" > <h2 align='center'> My Latest Blogs  </h2> </a> </body> </html>'''
	return HttpResponse(html)
	
def get_all_blogs(request):
	#if not request.user.is_authenticated():
		#return redirect('/get_name/')
	all_blogs=Blog.objects.all()
	return render(request,'myapp/index.html',{'blogs_list':all_blogs})
	#data=serializers.serialize("xml",all_blogs);
	#return HttpResponse(data,content_type="application/xhtml+xml")

def get_latest_blogs(request):
	blogs_latest=Blog.objects.order_by('pub_date')[:2]
	#data=serializers.serialize("xml",blogs_latest);
	#return HttpResponse(data,content_type="application/xhtml+xml")
	return render(request,'myapp/index.html',{'blogs_list':blogs_latest})
	
def get_blog(request,ques_id):
	try:
		offset=int(ques_id)
	except ValueError:
		raise Http404()
	try:
		blog=Blog.objects.get(pk=ques_id)
	except Blog.DoesNotExist:
		raise Http404("Question Doesnot exist")
	#data=serializers.serialize("xml",[blog])
	#return HttpResponse(data,content_type="application/xhtml+xml")
	blogs_latest=Blog.objects.order_by('pub_date')
	return render(request,'myapp/blog.html',{'b':blog,'blogs_list':blogs_latest})
	

	

