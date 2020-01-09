#Django 相关学习笔记

## 请求与响应


###第一步：生成工程

    django-admin startproject mysite

####结构特点

外层的mysite/目录与Django无关，只是你项目的容器，可以任意重命名。

manage.py：一个命令行工具，用于与Django进行不同方式的交互脚本，非常重要！

内层的mysite/目录是真正的项目文件包裹目录，它的名字是你引用内部文件的包名，例如：mysite.urls。

mysite/__init__.py:一个定义包的空文件。

mysite/settings.py:项目的主配置文件，非常重要！

mysite/urls.py:路由文件，所有的任务都是从这里开始分配，相当于Django驱动站点的内容表格，非常重要！

mysite/wsgi.py:一个基于WSGI的web服务器进入点，提供底层的网络通信功能，通常不用关心。

### 新建项目

    python manage.py startapp polls
    
### 在views.py中编写视图

### 在项目中新增 urls.py 作为路由路径，作为调用该视图

### 在主url中通过include引用路由文件

## 模型与后台

在models.py中定义模型model,也就是建立数据库表的布局

####启用模型

创建该app对应的数据库表结构

为Question和Choice对象创建基于Python的数据库访问API

要将应用添加到项目中，需要在INSTALLED_APPS设置中增加指向该应用的配置文件的链接。对于本例的投票应用，它的配置类文件PollsConfig是polls/apps.py，所以它的点式路径为polls.apps.PollsConfig。我们需要在INSTALLED_APPS中，将该路径添加进去

    python manage.py makemigrations polls
    
    python manage.py sqlmigrate polls 0001
    
    python manage.py migrate
    
#### 执行django

    python manage.py runserver 127.0.0.1:8787
    
