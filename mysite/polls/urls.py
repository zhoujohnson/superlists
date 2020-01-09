from django.urls import path

from . import views

app_name ='polls'  # 注册命名空间



urlpatterns = [
    path('',views.index,name='index'),
    # path('',views.detail,name='detail'),
    path('<int:question_id>/',views.detail,name ='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),

]