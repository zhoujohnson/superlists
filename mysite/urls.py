# 路由是浏览器输入url，在Django服务器响应url的转发中心。路由都
# 写在urls文件里，它将浏览器输入的url映射到相应的业务处理逻辑也
# 就是视图。
from django.contrib import admin
from django.conf.urls import include,url
'''include的背后是一种即插即用的思想。项目根路由不关心具体app的
路由策略，只管往指定的二级路由转发，实现了应用解耦。app所属的二
级路由可以根据自己的需要随意编写，不会和其它的app路由发生冲突。
app目录可以放置在任何位置，而不用修改路由。这是软件设计里很常见
的一种模式。'''
# from django.urls import path
# from polls import views  # 需要先导入对应app中的views文件
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path(r'^polls',view.index))   # 我们添加这条路由，重点是路由
# ]

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^polls',include('polls.urls'))
]
