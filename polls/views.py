# 路由转发用户请求到视图函数。视图函数处理用户请求，也就是编写业务处理逻辑
# 一般都放在views.py中


from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# 第一个参数必须是request，名字可以改，但是最好不要，这是潜规则。
# request参数封装了用户的所有内容

# 不能直接返回字符串，必须由HttpRequese类封装起来，才能被HTTP
# 协议识别
def index(request):
    # return HttpResponse("Hello,world,You're at the polls index")
    # render方法使用数据字典和请求元数据，渲染一个指定的HTML模板。
    # 其多个参数中，第一个参数必须是request，第二个是模板
    return render(request,'index.html')