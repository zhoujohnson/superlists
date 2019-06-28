#coding=utf8
from conf import config
import httplib
import urllib
import urllib2
class Data_send_glsx():
    def send_data(self,cc,cn,ap,at,rt,e,rut,r,hc,ru,bc):
        post_dict = {}
        post_dict["cc"] = cc  #cc：用例编码必填
        post_dict["cn"] = cn  #cn：用例名称必填
        post_dict["ap"] = ap  #ap：测试用例机器所在地址必填
        post_dict["at"] = at  #at：用例调用时间，时间精确到秒，格式yyyyMMddHHmmss必填
        post_dict["rt"] = rt  #rt：用例响应时间允许为空
        post_dict["e"] = e  #e：耗时(ms)必填
        post_dict["rut"] = rut  #rut：成功与否标志位必填
        post_dict["r"] = r  #r：返回结果必填
        post_dict["hc"] = hc  #hc：http响应码必填
        post_dict["ru"] = ru  #ru：请求url必填
        post_dict["bc"] = bc  #bc：业务代码允许为空

        test_data_encode = urllib.urlencode(post_dict)
        request = config.GRC_Address.address

        req = urllib2.Request(url=request,data=test_data_encode)

        res_data = urllib2.urlopen(req)

        res = res_data.read()
        print res

if __name__ == "__main__":
    cc = "ddbox-login"
    cn = "ddbox测试接口"
    ap = "192.168.3.238"
    at = "20150616165530"
    rt = "20150616165530"
    e = "30"
    rut = "1"
    r = "{errorCode:1}"
    hc = "201"
    ru = "htpp://diddihu.com.cn/login.shtml"
    bc = "1"
    Data_send_glsx().send_data(cc,cn,ap,at,rt,e,rut,r,hc,ru,bc)


