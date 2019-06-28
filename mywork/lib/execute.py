#coding=utf8
from django.shortcuts import render_to_response
from django import forms
from mywork.models import User
from mywork.models import Glsx_test_case
from mywork.models import Glsx_test_case_params
from django.http import HttpResponseRedirect
import libdatabase
import urllib
import httplib
import urllib2
import re
import convert_dict
import httpGetOrPost
def execute_single(num,test_id):
	#定义存储数据的list
	singleCase_list = []
	#定义成功标志位flag
	flag = "PASS"
	#通过id从数据库查询到该对应的记录
	case = Glsx_test_case.objects.get(id = test_id)
	#定义create_id
	create_id = case.id
	#定义create_code
	create_code = case.case_code
	#定义create_name
	create_name = case.case_name
	#定义create_hostUrl
	create_hostUrl = case.request_url
	#定义param,按倒序排列
	param = Glsx_test_case_params.objects.filter(glsx_test_case_id = test_id).order_by("-order")
	length = len(list(param))
	
	if length<3:
		create_url = create_hostUrl
		response_content = "Error URL or Param"
		expectValue = ""
		flag = "FAIL"
		request_time = "0"
		response_time = "0"
		response_code = "0"
		cost = "0"
		
		singleCase_list.append(int(num))
		singleCase_list.append(int(test_id))
		singleCase_list.append(create_name)
		singleCase_list.append(create_url)
		singleCase_list.append(response_content)
		singleCase_list.append(request_time)
		singleCase_list.append(response_time)
		singleCase_list.append(cost)
		singleCase_list.append(response_code)
		singleCase_list.append(expectValue)
		singleCase_list.append(flag)
		return singleCase_list
		
	
	else:
		#获取到预期值expectValue
		expectValue = param[0].param_value
		#获取到是否有关联函数的字段和值
		related_param_name = param[1].param_name
		related_param_value = param[1].param_value
		
		param_new = param[2:]
		list_names = []
		list_values = []
		response_content=""
		for param_i in param_new:
			list_names.append(param_i.param_name)
			list_values.append((param_i.param_value).encode("utf8"))
		
		#对读取到的参数进行处理，需要计算的进行计算，需要替换的进行替换,其中参数包括用例的ID，所有参数名称的列表，所有参数值的列表，关联函数参数的名称、关联函数参数的值
		new_dict = convert_dict.convert_dict(list_names,list_values,related_param_name,related_param_value)
		
		post_data = urllib.urlencode(new_dict)
		create_url = create_hostUrl + "?" + post_data
		
		
		#对请求的URL进行HTTP请求处理,http_list中包括请求时间、响应时间、耗时、响应的内容和响应码
		http_list = httpGetOrPost.getOrPost(create_hostUrl,new_dict)
		#return http_list
		request_time = http_list[0]
		response_time = http_list[1]
		cost = http_list[2]
		response_content = http_list[3]
		response_code = http_list[4]
		
		#验证测试结果
		test_virify = re.search(expectValue,response_content)
	
		if test_virify:
			flag = "PASS"
		else:
			flag = "FAIL"
		
		
		#处理获取验证码--modify date2016-2-26
		#定义获取验证码返回的字段值，后面进行比较
		checkCode_string = '{"errorCode":0,"msg":"success","isPage":0,"reservedVal":"","result":null}'
		if re.match(checkCode_string,response_content):
			#进入数据库查询该验证码的值
			conn = libdatabase.connMySql(host='192.168.1.39', user='test_yangqw', passwd='75719d8b', db="cyb_os", port=3306, charset='utf8')
			sql = "SELECT content FROM platform_message_send_log ORDER BY create_time DESC"
			res =  libdatabase.sqlSelect(sql,conn)
			conn.close()
			response_content1 = res[0][0].encode("utf8")
			message_code1 = re.search("(\d+)",response_content1)
			message_code = message_code1.group(1)
			response_content = "checkCode:"+message_code
		
		
		singleCase_list.append(int(num))
		singleCase_list.append(int(test_id))
		singleCase_list.append(create_name)
		singleCase_list.append(create_url)
		singleCase_list.append(response_content)
		singleCase_list.append(request_time)
		singleCase_list.append(response_time)
		singleCase_list.append(cost)
		singleCase_list.append(response_code)
		singleCase_list.append(expectValue)
		singleCase_list.append(flag)
		
		
		
		
		return singleCase_list
