#coding=utf-8
import urllib
import urllib2
import shutil
import Current_time
import time_diff
import httplib

def getOrPost(request_hostUrl,dict_data):
	post_data = urllib.urlencode(dict_data)
	create_url = request_hostUrl + "?" + post_data
	
	#将请求的url拆分出来
	create_url = create_url.split("//")[1]
	list_url = create_url.split("/")
	list_host_port = list_url[0].split(":")
	req_host = list_host_port[0]
	req_port = list_host_port[1]
	req_postUrl = "/"+"/".join(request_hostUrl.split("//")[1].split("/")[1:])
	req_getUrl = "/"+"/".join(list_url[1:])
	
	
	
	try:
			try:
				httpConn = httplib.HTTPConnection(host=req_host,port=int(req_port))
				#定义一个空的列表，用来存放请求时间，返回时间，请求消耗的时间以及返回结果
				array = []
				#记录请求前的系统时间
				request_time = Current_time.interval_time()
				#获取系统当前时间
				request_time_now = request_time[0]
				#获取系统当前时间戳
				request_time_stamp = request_time[1]
				#将请求时间放入到列表中
				#**********************************GET请求服务器
				httpConn.request('GET',req_getUrl)
				#记录请求后的系统时间
				response_time = Current_time.interval_time()
				#获取系统当前时间
				response_time_now = response_time[0]
				#获取系统当前时间戳
				response_time_stamp = response_time[1]
				#获取请求的响应对象
				result=httpConn.getresponse()
				#计算请求前后的时间差,单位为毫秒
				cost = round((response_time_stamp - request_time_stamp) * 1000,5)
				#服务器返回的响应数据
				url_content = result.read()[:200]
				#服务器返回的响应码
				url_code = result.status
				#将请求时间、响应时间、耗时、响应的内容和响应码依次放入到列表中
				array.append(request_time_now)
				array.append(response_time_now)
				array.append(cost)
				array.append(url_content)
				array.append(url_code)
				return array
				
				
			except:
				#定义一个空的列表，用来存放请求时间，返回时间，请求消耗的时间以及返回结果
				array = []
				#记录请求前的系统时间
				request_time = Current_time.interval_time()
				#获取系统当前时间
				request_time_now = request_time[0]
				#获取系统当前时间戳
				request_time_stamp = request_time[1]
				#将请求时间放入到列表中
				headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"}
				#httpConn.request('POST',req_postUrl,post_data)
				#**********************************POST请求服务器
				req = urllib2.Request(request_hostUrl,post_data,headers)
				result = urllib2.urlopen(req)
				#记录请求后的系统时间
				response_time = Current_time.interval_time()
				#获取系统当前时间
				response_time_now = response_time[0]
				#获取系统当前时间戳
				response_time_stamp = response_time[1]
				#计算请求前后的时间差,单位为毫秒
				cost = round((response_time_stamp - request_time_stamp) * 1000,5)
				#服务器返回的响应数据
				url_content = result.read()[:200]
				#服务器返回的响应码
				url_code = result.code
				#将请求时间、响应时间、耗时、响应的内容和响应码依次放入到列表中
				array.append(request_time_now)
				array.append(response_time_now)
				array.append(cost)
				array.append(url_content)
				array.append(url_code)
				return array

	
				
	except Exception,e:
		#当出现异常时
		#定义一个空的列表，用来存放请求时间，返回时间，请求消耗的时间以及返回结果
		array = []
		#记录请求前的系统时间
		request_time = Current_time.interval_time()
		#获取系统当前时间
		request_time_now = request_time[0]
		#获取系统当前时间戳
		request_time_stamp = request_time[1]
		url_content = str(e)
		#将请求时间、响应时间、耗时、响应的内容和响应码依次放入到列表中
		array.append(request_time_now)
		array.append(request_time_now)
		array.append(0)
		array.append(url_content)
		array.append("0")
		return array
			



