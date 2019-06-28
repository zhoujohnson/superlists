#coding=utf-8
from django.db import models
from django.contrib import admin

	
class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

class UserAdmin(admin.ModelAdmin):
	list_display = ('username','password')	

admin.site.register(User,UserAdmin)


class Glsx_test_case(models.Model):
	case_code = models.CharField(max_length=100)
	case_name = models.CharField(max_length=100)
	request_url = models.CharField(max_length=200)
	case_desc = models.CharField(max_length=300)
	
class Glsx_test_case_params(models.Model):
	param_name = models.CharField(max_length=100)
	param_value = models.CharField(max_length=100)
	order = models.IntegerField()
	glsx_test_case = models.ForeignKey(Glsx_test_case)
	
class Glsx_test_result(models.Model):
	case_id = models.IntegerField(verbose_name="用例编号",null=True)
	case_name = models.CharField(max_length=100,verbose_name="用例名称",null=True)
	request_url = models.TextField(verbose_name="请求的URL",null=True)
	response_content = models.TextField(verbose_name="响应内容",null=True)
	request_time = models.CharField(max_length=100,verbose_name="请求时间",null=True)
	response_time = models.CharField(max_length=100,verbose_name="响应时间",null=True)
	cost = models.CharField(max_length=100,verbose_name="耗时(ms)",null=True)
	response_code = models.CharField(max_length=100,verbose_name="响应码",null=True)
	expectValue = models.TextField(verbose_name="预期结果",null=True)
	execute_condition = models.CharField(max_length=100,verbose_name="执行情况",null=True)
	
	
	