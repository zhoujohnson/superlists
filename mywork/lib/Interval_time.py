__author__ = 'Administrator'
#coding=utf8
import time
from conf import config
def rest_time():
    #定义间隔时间
    n = config.Frent_query.n
    print "间隔时间为：",n,"秒,请等待........................."
    time.sleep(n)

if __name__ == "__main__":
    rest_time()
