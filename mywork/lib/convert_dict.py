#coding=utf-8
from django.shortcuts import render_to_response
from django import forms
from mywork.models import User
from mywork.models import Glsx_test_case
from mywork.models import Glsx_test_case_params
from django.http import HttpResponseRedirect
import execute
import sign_md5
import urllib
import httplib
import urllib2
import re

def convert_dict(list_param_names,list_param_values,related_param_name,related_param_value):
	#对读取到的参数进行处理，需要计算的进行计算，需要替换的进行替换,其中参数包括用例的ID，所有参数名称的列表，所有参数值的列表，关联函数参数的名称、关联函数参数的值
	#定义一个约定的字段，来判断list_param_values中是否有需要替换的值
	check_value = "relation"
	
	#定义一个list，用来存储需要转换的参数名称
	convert_param_name_list = []
	#定义需要调用的测试用例的ID
	related_ID = 0
	
	new_dict = dict(zip(list_param_names,list_param_values))
	
	for i in range(len(list_param_values)):
		#判断是否可以匹配到包含有该字符串的参数的值
		match_value = re.match(check_value,list_param_values[i])
		if match_value:
			convert_param_name_list.append(list_param_names[i])
			related_ID = int(list_param_values[i].replace(check_value,""))
	
	#若匹配到了该字段，说明该参数需要调用其他接口来获取所需的值,该接口的ID为related_ID
	if convert_param_name_list:
		data_list = execute.execute_single(1,related_ID)
		#取出调用该接口后接口返回的值
		require_value = data_list[4]
		#去掉返回值中所有的"
		require_value_new = require_value.replace('"',"")
		#定义一个list来存储匹配到所有的字符串
		match_list = []
		for j in convert_param_name_list:
			pattern_value = j + ":" + "\w+"
			pattern_string = re.search(pattern_value,require_value_new)
			match_list.append(pattern_string.group())
		#把取出的列表组合成字典
		name_list = []
		value_list = []
		for k in match_list:
			x = k.split(":")
			name_list.append(x[0])
			value_list.append(x[1])
		convert_string_dict = dict(zip(name_list,value_list))
		
		for t in range(len(list_param_names)):
			if convert_string_dict.get(list_param_names[t]):
				list_param_values[t] = convert_string_dict.get(list_param_names[t])
				
		new_dict = dict(zip(list_param_names,list_param_values))
		
		if related_param_value == "null":
			return new_dict
			
		else:
			for m in range(len(list_param_values)):
			#在参数值列表中查找某个参数为关联函数的参数名
				if list_param_values[m] == related_param_name:
					del new_dict[list_param_names[m]]
					real_value = sign_md5.sign_md5(new_dict)
					new_dict[list_param_names[m]] = real_value
					return new_dict
			
			
	else:
		if related_param_value == "null":
			new_dict = dict(zip(list_param_names,list_param_values))
			return new_dict
		else:
			for m in range(len(list_param_values)):
			#在参数值列表中查找某个参数为关联函数的参数名
				if list_param_values[m] == related_param_name:
					del new_dict[str(list_param_names[m])]					
					real_value = sign_md5.sign_md5(new_dict)
					new_dict[str(list_param_names[m])] = real_value
					return new_dict
