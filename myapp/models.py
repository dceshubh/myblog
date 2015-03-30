from django.db import models
import datetime

# Create your models here.
class Blog(models.Model):
	title=models.CharField('Enter the Title of your blog ',max_length=100)
	pub_date=models.DateTimeField('date published',default=datetime.datetime.now())
	body=models.CharField('Enter the body of your blog',max_length=5000)
	
	def __str__(self):
		return self.title
		
class Comments(models.Model):
	blog=models.ForeignKey(Blog)
	text=models.CharField('Enter your comment', max_length=1000)
	username=models.CharField('Enter your name',max_length=50,default='anonymous')
	photo=models.ImageField(upload_to='images',default='')
	comment_date=models.DateTimeField('comment date',default=datetime.datetime.now())
	
	def __str__(self):
		return self.text[:20]

	
