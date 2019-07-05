from django.db import models

# Create your models here.
# 要继承这个类，固定写法

# class UserInfo(models.Model):
#     user = models.CharField(max_length=32)
#     pwd = models.CharField(max_length=32)

# 1  然后再命令行中输入 python manage.py makemigrations , 可以看到再migrations中生成了0001_initial.py文件

# 2  再输入命令 python manage.py migrate