"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
'''include的背后是一种即插即用的思想。项目根路由不关心具体app的
路由策略，只管往指定的二级路由转发，实现了应用解耦。app所属的二
级路由可以根据自己的需要随意编写，不会和其它的app路由发生冲突。
app目录可以放置在任何位置，而不用修改路由。这是软件设计里很常见
的一种模式。'''
# from django.urls import path
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^polls',include('polls.urls'))
]
