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
	
	#�������url��ֳ���
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
				#����һ���յ��б������������ʱ�䣬����ʱ�䣬�������ĵ�ʱ���Լ����ؽ��
				array = []
				#��¼����ǰ��ϵͳʱ��
				request_time = Current_time.interval_time()
				#��ȡϵͳ��ǰʱ��
				request_time_now = request_time[0]
				#��ȡϵͳ��ǰʱ���
				request_time_stamp = request_time[1]
				#������ʱ����뵽�б���
				#**********************************GET���������
				httpConn.request('GET',req_getUrl)
				#��¼������ϵͳʱ��
				response_time = Current_time.interval_time()
				#��ȡϵͳ��ǰʱ��
				response_time_now = response_time[0]
				#��ȡϵͳ��ǰʱ���
				response_time_stamp = response_time[1]
				#��ȡ�������Ӧ����
				result=httpConn.getresponse()
				#��������ǰ���ʱ���,��λΪ����
				cost = round((response_time_stamp - request_time_stamp) * 1000,5)
				#���������ص���Ӧ����
				url_content = result.read()[:200]
				#���������ص���Ӧ��
				url_code = result.status
				#������ʱ�䡢��Ӧʱ�䡢��ʱ����Ӧ�����ݺ���Ӧ�����η��뵽�б���
				array.append(request_time_now)
				array.append(response_time_now)
				array.append(cost)
				array.append(url_content)
				array.append(url_code)
				return array
				
				
			except:
				#����һ���յ��б������������ʱ�䣬����ʱ�䣬�������ĵ�ʱ���Լ����ؽ��
				array = []
				#��¼����ǰ��ϵͳʱ��
				request_time = Current_time.interval_time()
				#��ȡϵͳ��ǰʱ��
				request_time_now = request_time[0]
				#��ȡϵͳ��ǰʱ���
				request_time_stamp = request_time[1]
				#������ʱ����뵽�б���
				headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"}
				#httpConn.request('POST',req_postUrl,post_data)
				#**********************************POST���������
				req = urllib2.Request(request_hostUrl,post_data,headers)
				result = urllib2.urlopen(req)
				#��¼������ϵͳʱ��
				response_time = Current_time.interval_time()
				#��ȡϵͳ��ǰʱ��
				response_time_now = response_time[0]
				#��ȡϵͳ��ǰʱ���
				response_time_stamp = response_time[1]
				#��������ǰ���ʱ���,��λΪ����
				cost = round((response_time_stamp - request_time_stamp) * 1000,5)
				#���������ص���Ӧ����
				url_content = result.read()[:200]
				#���������ص���Ӧ��
				url_code = result.code
				#������ʱ�䡢��Ӧʱ�䡢��ʱ����Ӧ�����ݺ���Ӧ�����η��뵽�б���
				array.append(request_time_now)
				array.append(response_time_now)
				array.append(cost)
				array.append(url_content)
				array.append(url_code)
				return array

	
				
	except Exception,e:
		#�������쳣ʱ
		#����һ���յ��б������������ʱ�䣬����ʱ�䣬�������ĵ�ʱ���Լ����ؽ��
		array = []
		#��¼����ǰ��ϵͳʱ��
		request_time = Current_time.interval_time()
		#��ȡϵͳ��ǰʱ��
		request_time_now = request_time[0]
		#��ȡϵͳ��ǰʱ���
		request_time_stamp = request_time[1]
		url_content = str(e)
		#������ʱ�䡢��Ӧʱ�䡢��ʱ����Ӧ�����ݺ���Ӧ�����η��뵽�б���
		array.append(request_time_now)
		array.append(request_time_now)
		array.append(0)
		array.append(url_content)
		array.append("0")
		return array
			



