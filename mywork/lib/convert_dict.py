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
	#�Զ�ȡ���Ĳ������д�����Ҫ����Ľ��м��㣬��Ҫ�滻�Ľ����滻,���в�������������ID�����в������Ƶ��б����в���ֵ���б������������������ơ���������������ֵ
	#����һ��Լ�����ֶΣ����ж�list_param_values���Ƿ�����Ҫ�滻��ֵ
	check_value = "relation"
	
	#����һ��list�������洢��Ҫת���Ĳ�������
	convert_param_name_list = []
	#������Ҫ���õĲ���������ID
	related_ID = 0
	
	new_dict = dict(zip(list_param_names,list_param_values))
	
	for i in range(len(list_param_values)):
		#�ж��Ƿ����ƥ�䵽�����и��ַ����Ĳ�����ֵ
		match_value = re.match(check_value,list_param_values[i])
		if match_value:
			convert_param_name_list.append(list_param_names[i])
			related_ID = int(list_param_values[i].replace(check_value,""))
	
	#��ƥ�䵽�˸��ֶΣ�˵���ò�����Ҫ���������ӿ�����ȡ�����ֵ,�ýӿڵ�IDΪrelated_ID
	if convert_param_name_list:
		data_list = execute.execute_single(1,related_ID)
		#ȡ�����øýӿں�ӿڷ��ص�ֵ
		require_value = data_list[4]
		#ȥ������ֵ�����е�"
		require_value_new = require_value.replace('"',"")
		#����һ��list���洢ƥ�䵽���е��ַ���
		match_list = []
		for j in convert_param_name_list:
			pattern_value = j + ":" + "\w+"
			pattern_string = re.search(pattern_value,require_value_new)
			match_list.append(pattern_string.group())
		#��ȡ�����б���ϳ��ֵ�
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
			#�ڲ���ֵ�б��в���ĳ������Ϊ���������Ĳ�����
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
			#�ڲ���ֵ�б��в���ĳ������Ϊ���������Ĳ�����
				if list_param_values[m] == related_param_name:
					del new_dict[str(list_param_names[m])]					
					real_value = sign_md5.sign_md5(new_dict)
					new_dict[str(list_param_names[m])] = real_value
					return new_dict
