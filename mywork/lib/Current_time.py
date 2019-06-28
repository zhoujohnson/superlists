#coding=utf8
import time
def interval_time():
	list = []
	now = time.time()
	now_struct = time.localtime(now)
	time_now = time.strftime("%Y-%m-%d %H:%M:%S",now_struct)
	list.append(time_now)
	list.append(now)
	return list