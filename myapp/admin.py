from django.contrib import admin
from myapp.models import Blog,Comments

# Register your models here.
class CommentInline(admin.TabularInline):
	model=Comments

class BlogAdmin(admin.ModelAdmin):
	fieldsets=[
	(None,                                   {'fields': ['title']}),
	(None,                                   {'fields': ['body']}),
	('Date Information',               {'fields':['pub_date'],
	'classes':['collapse']}),
	]
	inlines=[CommentInline]
	#fields=['pub_date','question_text']
admin.site.register(Blog,BlogAdmin)

# Register your models here.
