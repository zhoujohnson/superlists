#coding=utf8
from django.shortcuts import render_to_response
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage,InvalidPage
from django import forms
from mywork.models import User
from mywork.models import Glsx_test_case
from mywork.models import Glsx_test_case_params
from mywork.models import Glsx_test_result
from django.http import HttpResponseRedirect
from lib import execute
from lib import libdatabase
from lib import getHostName
import urllib
import time
import httplib
import urllib2
import re

# Create your views here.

#定义表单模型
class UserForm(forms.Form):
	username = forms.CharField(label='用户名',max_length=100)
	password = forms.CharField(label='密码',widget=forms.PasswordInput())

#登录
def login(rq):
	uf = UserForm(rq.POST)
	if uf.is_valid():
		#获取表单用户名和密码
		username = uf.cleaned_data['username']
		password = uf.cleaned_data['password']
		#获取的表单数据与数据库进行比较
		user = User.objects.filter(username__exact = username,password__exact = password)
		if user:
			return HttpResponseRedirect('/index/'+username)
		else:
			return HttpResponseRedirect('/login/')
	
	else:
		uf = UserForm()
		return render_to_response('test/login.html',{'uf':uf})

def index(rq,host):
	display_num = 4
	try:
		page = int(rq.GET.get('page','1'))
		
		if page<1:
			page = 1
	except ValueError:
		page = 1
	
	data = Glsx_test_case.objects.all().order_by("-id")
	p = Paginator(data,10)
	try:
		winloglist = p.page(page)
	except (PageNotAnInteger,EmptyPage,InvalidPage):
		winloglist = p.page(1)
	
	try:
		yqw_previous = winloglist.previous_page_number()
	except (PageNotAnInteger,EmptyPage,InvalidPage):
		yqw_previous = 1
		
	try:
		yqw_next = winloglist.next_page_number()
	except (PageNotAnInteger,EmptyPage,InvalidPage):
		yqw_next = p.num_pages
	
	tatol_page = p.num_pages
	#return render_to_response("test/aaa.html",{'yqw_previous':yqw_previous})
	
	page_range = p.page_range[page-1:int(page)+display_num]
	
	return render_to_response("test/index.html",locals())
	#return render_to_response("test/index.html",{'data':data,'host':host})


def case_detail(rq,case_id,action):
	if action == "modify":
		param = Glsx_test_case.objects.get(id=case_id)
		return render_to_response('test/case_act.html',{'param':param,'action':action,"case_id":case_id})
		
	elif action == "add":
		return render_to_response('test/case_act.html',{'action':action,"case_id":case_id})
		
	elif action == "del":
		param = Glsx_test_case.objects.get(id=case_id)
		return render_to_response('test/case_act.html',{'param':param,'action':action,"case_id":case_id})
			

def case_act(rq,my_case_id):
	if rq.POST.has_key('case_act') and rq.POST.has_key('case_id') and rq.POST.has_key('case_code') and rq.POST.has_key('case_name') and rq.POST.has_key('request_url') and rq.POST.has_key('case_desc'): 
		if rq.POST['case_act'] == 'modify': 
			#获取用例对象
			case_list = Glsx_test_case.objects.get(id=my_case_id)
			#修改case_id
			case_list.id = rq.POST['case_id']
			#修改case_code
			case_list.case_code = rq.POST["case_code"]
			#修改case_name
			case_list.case_name = rq.POST["case_name"]
			#修改request_url
			case_list.request_url = rq.POST["request_url"]
			#修改case_desc
			case_list.case_desc = rq.POST["case_desc"]
			#保存修改的值
			case_list.save()
			return HttpResponseRedirect('/index/test')
			
	elif rq.POST.has_key('case_act1') and rq.POST['case_act1'] == 'add':
		p = Glsx_test_case.objects.create(id = rq.POST['case_id'], case_code = rq.POST['case_code'],case_name = rq.POST['case_name'],request_url = rq.POST['request_url'],case_desc = rq.POST['case_desc'])
		return HttpResponseRedirect('/index/test')
	
	elif rq.POST.has_key('case_act2') and rq.POST['case_act2'] == 'del' and rq.POST.has_key('case_id'):
		case_id = rq.POST["case_id"]
		p = Glsx_test_case.objects.get(id = case_id)
		p.delete()
		return HttpResponseRedirect('/index/test')


def param_detail(rq,case_id):
	param = Glsx_test_case_params.objects.filter(glsx_test_case=case_id).order_by('order')
	if rq.GET.has_key('act') and rq.GET.has_key("step_id"):
		step_id = rq.GET["step_id"]
		if rq.GET['act'] == 'modify':
			param_i = param.get(id=step_id)
			return render_to_response('test/param_act.html',{'param_i':param_i,'act':'modify',"id":step_id,"case_id":case_id})
		
	elif rq.GET.has_key('act') and rq.GET['act'] == 'add':
		return render_to_response('test/param_act.html',{'act':'add','case_id':case_id})
	
	elif rq.GET.has_key('act') and rq.GET.has_key("step1_id"):
		step_id = rq.GET["step1_id"]
		if rq.GET['act'] == 'del':
			param1_i = param.get(id=step_id)
			return render_to_response('test/param_act.html',{"act":"del","param1_i":param1_i,"id":step_id,"case_id":case_id})
		
	return render_to_response("test/detail.html",{'case_id':case_id,'param':param})
	
def param_act(rq,my_step_id):
	if rq.POST.has_key('param_act') and rq.POST.has_key('param_id') and rq.POST.has_key('param_name') and rq.POST.has_key('param_value') and rq.POST.has_key('order'): 
		if rq.POST['param_act'] == 'modify': 
			#获取参数对象
			param_list = Glsx_test_case_params.objects.get(id=rq.POST['param_id'])
			#修改param_id
			param_test_id = rq.POST['param_id']
			#修改param_name
			param_list.param_name = rq.POST["param_name"]
			#修改param_value
			param_list.param_value = rq.POST["param_value"]
			#修改order
			param_list.order = rq.POST["order"]
			#保存修改的值
			param_list.save()
			return HttpResponseRedirect('/index/'+my_step_id+"/params")
	elif rq.POST.has_key('param_act1') and rq.POST['param_act1'] == 'add':
		p = Glsx_test_case_params.objects.create(id = rq.POST['param_id'], param_name = rq.POST['param_name'],param_value = rq.POST['param_value'],order = rq.POST['order'],glsx_test_case_id = my_step_id)
		return HttpResponseRedirect('/index/'+my_step_id+"/params")
	
	elif rq.POST.has_key('param_act2') and rq.POST['param_act2'] == 'del' and rq.POST.has_key('param_id'):
		param_id = rq.POST["param_id"]
		p = Glsx_test_case_params.objects.get(id = param_id)
		p.delete()
		return HttpResponseRedirect('/index/'+my_step_id+"/params")
	
		

def executeTestCase(rq,test_id):
	result_list = execute.execute_single(1,test_id)
	table_name = "Table" + str(time.time()).split(".")[0]
	conn = libdatabase.connMySql()
	sql = '''
		CREATE TABLE ''' + table_name + '''(
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `case_id` int(11) DEFAULT NULL,
  `case_name` varchar(100) DEFAULT NULL,
  `request_url` longtext,
  `response_content` longtext,
  `request_time` varchar(100) DEFAULT NULL,
  `response_time` varchar(100) DEFAULT NULL,
  `cost` varchar(100) DEFAULT NULL,
  `response_code` varchar(100) DEFAULT NULL,
  `expectValue` longtext,
  `execute_condition` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8
			'''

	libdatabase.sqlSelect(sql,conn)
	
	sql1 = '''
        insert into ''' + table_name + ''' values(%d,%d,\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')
         ''' % (result_list[0],result_list[1],result_list[2],result_list[3],re.sub("\'t|\'s","",result_list[4].decode("utf8")),result_list[5],result_list[6],result_list[7],result_list[8],result_list[9],result_list[10])
	libdatabase.insert_data(sql1,conn)
	
	conn.close()
	
	
	#先删除数据库中原有的数据，然后再进行创建
	#my = Glsx_test_result.objects.all()
	#my.delete()
	#p = Glsx_test_result.objects.create(case_id=result_list[1],case_name=result_list[2],request_url=result_list[3],response_content=result_list[4],request_time=result_list[5],response_time=result_list[6],cost=result_list[7],response_code=result_list[8],expectValue=result_list[9],execute_condition=result_list[10])
	#将该数据插入到数据库中
	#return render_to_response('test/aaa.html',{'sql1':sql1})
	return render_to_response('test/createTestCase.html',{'result_list':result_list,'table_name':table_name})
	#return render_to_response('test/test.html',{'result_list':result_list})

def executeManyPolicy(rq):
	return render_to_response("test/policy.html")
	

def executeManyTestCase(rq):
	#首先获取到该数据库中所有的ID，以便后面传入进来的ID进行对比，若输入的ID不存在于数据库中，则直接跳过
	data = Glsx_test_case.objects.values("id")
	#定义存储所有的id的列表all_id
	all_id = []
	for data_i in data:
		i = data_i["id"]
		all_id.append(i)
	#return render_to_response("test/aaa.html",{'all_id':all_id})
	#定义一个list,用来存储数据
	multi_result_list = []
	#定义一个list，用来存储querySet
	querySetList = []
	#定义循环标志i
	i = 0
	#定义循环标志j
	j = 0
	
	if rq.POST.has_key("manyid") and rq.POST.has_key("freqid") and rq.POST.has_key("timesleep"):
		string_id = rq.POST["manyid"]
		frequency = rq.POST["freqid"]
		timesleep = rq.POST["timesleep"]
		
		#如果manyid的值为all，则执行所有的测试用例;否则执行输入的ID
		if string_id == "all":
			try:
				convert_frequency = int(frequency)
				convert_timesleep = int(timesleep)
				while i < convert_frequency:
					i = i + 1
					time.sleep(convert_timesleep)
					
					for id in all_id:
						j = j + 1
						singleCase_list = execute.execute_single(j,id)
						#querySetList.append(Glsx_test_result(id=singleCase_list[0],case_id=singleCase_list[1],case_name=singleCase_list[2],request_url=singleCase_list[3],response_content=singleCase_list[4],request_time=singleCase_list[5],response_time=singleCase_list[6],cost=singleCase_list[7],response_code=singleCase_list[8],expectValue=singleCase_list[9],execute_condition=singleCase_list[10]))
						multi_result_list.append(singleCase_list)
				
				#将该多条数据添加到数据库中
				#先删除数据库中原有的数据，然后再进行创建
				#my = Glsx_test_result.objects.all()
				#my.delete()
				#Glsx_test_result.objects.bulk_create(querySetList)
				
				#创建数据库，并写入数据
				table_name = "Table" + str(time.time()).split(".")[0]
		
				conn = libdatabase.connMySql()
				sql = '''
				CREATE TABLE ''' + table_name + '''(
				`id` int(11) NOT NULL AUTO_INCREMENT,
				`case_id` int(11) DEFAULT NULL,
				`case_name` varchar(100) DEFAULT NULL,
				`request_url` longtext,
				`response_content` longtext,
				`request_time` varchar(100) DEFAULT NULL,
				`response_time` varchar(100) DEFAULT NULL,
				`cost` varchar(100) DEFAULT NULL,
				`response_code` varchar(100) DEFAULT NULL,
				`expectValue` longtext,
				`execute_condition` varchar(100) DEFAULT NULL,
				PRIMARY KEY (`id`)
				) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8
				'''
		
				libdatabase.sqlSelect(sql,conn)		
				sql1 = '''
					insert into ''' + table_name + ''' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
					'''
				
				libdatabase.insert_manyData(sql1,multi_result_list,conn)
				conn.close()
												
				return render_to_response("test/createManyTestCase.html",{'multi_result_list':multi_result_list,'table_name':table_name})
			except:
				return render_to_response("test/policy.html")

				
		if not re.search(",",string_id) and int(string_id):
			try:
				convert_frequency = int(frequency)
				convert_timesleep = int(timesleep)
				while i < convert_frequency:
					i = i + 1
					time.sleep(convert_timesleep)
					
					singleCase_list = execute.execute_single(j,int(string_id))
					#querySetList.append(Glsx_test_result(id=singleCase_list[0],case_id=singleCase_list[1],case_name=singleCase_list[2],request_url=singleCase_list[3],response_content=singleCase_list[4],request_time=singleCase_list[5],response_time=singleCase_list[6],cost=singleCase_list[7],response_code=singleCase_list[8],expectValue=singleCase_list[9],execute_condition=singleCase_list[10]))
					multi_result_list.append(singleCase_list)
				
				#将该多条数据添加到数据库中
				#先删除数据库中原有的数据，然后再进行创建
				#my = Glsx_test_result.objects.all()
				#my.delete()
				#Glsx_test_result.objects.bulk_create(querySetList)
				
				#创建数据库，并写入数据
				table_name = "Table" + str(time.time()).split(".")[0]
		
				conn = libdatabase.connMySql()
				sql = '''
				CREATE TABLE ''' + table_name + '''(
				`id` int(11) NOT NULL AUTO_INCREMENT,
				`case_id` int(11) DEFAULT NULL,
				`case_name` varchar(100) DEFAULT NULL,
				`request_url` longtext,
				`response_content` longtext,
				`request_time` varchar(100) DEFAULT NULL,
				`response_time` varchar(100) DEFAULT NULL,
				`cost` varchar(100) DEFAULT NULL,
				`response_code` varchar(100) DEFAULT NULL,
				`expectValue` longtext,
				`execute_condition` varchar(100) DEFAULT NULL,
				PRIMARY KEY (`id`)
				) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8
				'''
		
				libdatabase.sqlSelect(sql,conn)		
				sql1 = '''
					insert into ''' + table_name + ''' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
					'''
				
				libdatabase.insert_manyData(sql1,multi_result_list,conn)
				conn.close()
												
				return render_to_response("test/createManyTestCase.html",{'multi_result_list':multi_result_list,'table_name':table_name})
			except:
				return render_to_response("test/policy.html")


		try:
			#格式的判断
			string_id = string_id.strip()
			search_comma = re.search(",",string_id)
			convert_frequency = int(frequency)
			convert_timesleep = int(timesleep)
			while i< convert_frequency:
				i = i + 1
				time.sleep(convert_timesleep)
				
				if search_comma:
					list_id = string_id.split(",")
					
					#处理包含有-的值
					#定义一个列表来存储转换后的值convert_list
					convert_list = []
					
					for list_id_value in list_id:
						try:
							if re.search("-",list_id_value):
								list_id_value_list = list_id_value.split("-")
								start_index = int(list_id_value_list[0])
								end_index = int(list_id_value_list[1])
								for list_id_value_list_i in range(start_index,end_index+1):
									convert_list.append(list_id_value_list_i)
							else:
								convert_list.append(list_id_value)
						except:
							return render_to_response("test/policy.html")
										
					
					for list_id_i in convert_list:
						try:
							convert_i = int(list_id_i)
							if convert_i in all_id:
								j = j + 1
								singleCase_list = execute.execute_single(j,convert_i)
								#querySetList.append(Glsx_test_result(id=singleCase_list[0],case_id=singleCase_list[1],case_name=singleCase_list[2],request_url=singleCase_list[3],response_content=singleCase_list[4],request_time=singleCase_list[5],response_time=singleCase_list[6],cost=singleCase_list[7],response_code=singleCase_list[8],expectValue=singleCase_list[9],execute_condition=singleCase_list[10]))
								multi_result_list.append(singleCase_list)
							else:
								continue
					
						except:
							return render_to_response("test/policy.html")
					
					
				else:
					return render_to_response("test/policy.html")
			
			#将该多条数据添加到数据库中
			#先删除数据库中原有的数据，然后再进行创建
			#my = Glsx_test_result.objects.all()
			#my.delete()
			#Glsx_test_result.objects.bulk_create(querySetList)
			
			#创建数据库，并写入数据
			table_name = "Table" + str(time.time()).split(".")[0]
		
			conn = libdatabase.connMySql()
			sql = '''
				CREATE TABLE ''' + table_name + '''(
				`id` int(11) NOT NULL AUTO_INCREMENT,
				`case_id` int(11) DEFAULT NULL,
				`case_name` varchar(100) DEFAULT NULL,
				`request_url` longtext,
				`response_content` longtext,
				`request_time` varchar(100) DEFAULT NULL,
				`response_time` varchar(100) DEFAULT NULL,
				`cost` varchar(100) DEFAULT NULL,
				`response_code` varchar(100) DEFAULT NULL,
				`expectValue` longtext,
				`execute_condition` varchar(100) DEFAULT NULL,
				PRIMARY KEY (`id`)
				) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8
			'''
		
			libdatabase.sqlSelect(sql,conn)			
			sql1 = '''
				insert into ''' + table_name + ''' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
				'''			
			libdatabase.insert_manyData(sql1,multi_result_list,conn)
			conn.close()
				
			return render_to_response("test/createManyTestCase.html",{'multi_result_list':multi_result_list,"table_name":table_name})
				
				
		
		except:
			return render_to_response("test/policy.html")
		
	else:
		return render_to_response("test/policy.html")
		
def outFile(rq,tableName):
	content = "文件生成成功，保存在服务器("+getHostName.getHostName()+")D盘目录下的test.xls文件"
	try:
		import xlrd,xlwt
		from xlutils.copy import copy
		filename = xlwt.Workbook(encoding="utf-8")
		sheet = filename.add_sheet("测试结果")
		sheet.write(0,0,"序号")
		sheet.write(0,1,"用例编号")
		sheet.write(0,2,"用例名称")
		sheet.write(0,3,"请求的URL")
		sheet.write(0,4,"响应内容")
		sheet.write(0,5,"请求时间")
		sheet.write(0,6,"响应时间")
		sheet.write(0,7,"耗时(ms)")
		sheet.write(0,8,"响应码")
		sheet.write(0,9,"预期结果")
		sheet.write(0,10,"测试结果[pass/fail]")
		file_name = "d:\\"+tableName+".xls"
		filename.save(file_name)
	
		i = 0
		conn = libdatabase.connMySql()
		sql = "select * from "+tableName
		all_data = libdatabase.sqlSelect(sql,conn)
		for all_data_i in all_data:
			i = i + 1
			rb = xlrd.open_workbook(file_name)
			wb = copy(rb)
			ws = wb.get_sheet(0)
			ws.write(i,0,all_data_i[0])
			ws.write(i,1,all_data_i[1])
			ws.write(i,2,all_data_i[2])
			ws.write(i,3,all_data_i[3])
			ws.write(i,4,all_data_i[4])
			ws.write(i,5,all_data_i[5])
			ws.write(i,6,all_data_i[6])
			ws.write(i,7,all_data_i[7])
			ws.write(i,8,all_data_i[8])
			ws.write(i,9,all_data_i[9])
			ws.write(i,10,all_data_i[10])
			wb.save(file_name)
			content = "文件生成成功，保存在服务器("+getHostName.getHostName()+")，文件路径为："+str(file_name)
		'''
		all_data = Glsx_test_result.objects.all()
		for all_data_i in all_data:
			i = i + 1
			rb = xlrd.open_workbook("d:\\test.xls")
			wb = copy(rb)
			ws = wb.get_sheet(0)
			ws.write(i,0,all_data_i.id)
			ws.write(i,1,all_data_i.case_id)
			ws.write(i,2,all_data_i.case_name)
			ws.write(i,3,all_data_i.request_url)
			ws.write(i,4,all_data_i.response_content)
			ws.write(i,5,all_data_i.request_time)
			ws.write(i,6,all_data_i.response_time)
			ws.write(i,7,all_data_i.cost)
			ws.write(i,8,all_data_i.response_code)
			ws.write(i,9,all_data_i.expectValue)
			ws.write(i,10,all_data_i.execute_condition)
			wb.save("d:\\test.xls")
		'''
	except Exception,e:
		content = str(e)
		

	return render_to_response("test/test.html",{"content":content})
	
	
