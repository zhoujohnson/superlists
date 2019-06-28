"""interface URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^login/','mywork.views.login'),
	url(r'^index/(?P<host>\w+)$','mywork.views.index'),
	url(r'^index/(?P<action>\w+)/(?P<case_id>\d+)','mywork.views.case_detail'),
	url(r'^index/(?P<my_case_id>\d+)/case_act/','mywork.views.case_act'),
	url(r'^index/(?P<case_id>\d+)/params$','mywork.views.param_detail'),
	url(r'^index/(?P<my_step_id>\d+)/param_act/','mywork.views.param_act'),
	url(r'^create/(?P<test_id>\d+)','mywork.views.executeTestCase'),
	url(r'^index/manyexcute/policy$','mywork.views.executeManyPolicy'),
	url(r'^index/manyexcute/result$','mywork.views.executeManyTestCase'),
	url(r'^outFile/(?P<tableName>\w+)','mywork.views.outFile'),
]
