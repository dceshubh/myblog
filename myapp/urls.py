from django.conf.urls import patterns, include, url
from myapp import views
from myapp.views import firstpage,get_all_blogs,get_latest_blogs,get_blog
from mylogin.views import get_name,log_out,sign_up,add_blog,add_user,publish_blog,authenticate_user,get_username,resend_link
from django.shortcuts import render

urlpatterns = patterns('',
    #url(r'^hello/$', hello),
    url(r'^$',get_name),
    url(r'^blogs/$',get_all_blogs),
    url(r'^latest/$',get_latest_blogs),
    #url(r'^$',get_all_questions_template),
    #url(r'^time/plus/(?P<offset>[A-Z\d]{1,2})/$', hours_ahead),
    #url(r'^current_time/$', current_date),
    #url(r'^server-time/$', current_date),
    #url(r'^questions/$', get_all_questions),
    url(r'^blogs/(?P<ques_id>\d+)/$', get_blog),
    url(r'^logout/',log_out),
    url(r'^signup/',sign_up),
    url(r'^addblog/',add_blog),
    url(r'^check/',add_user),
    url(r'^add/',publish_blog),
    url(r'^activate/',authenticate_user,name='main'),
    url(r'^frgpwd/',get_username),
    url(r'^resend/',resend_link),
    #url(r'^pwdsent/',send_password),


    )

