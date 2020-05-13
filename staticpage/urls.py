from django.urls import path, re_path
from . import views

urlpatterns = [

    # Create a page 创建页面
    path('', views.page_create, name='page_create'),

    # Page detail 展示页面详情。动态URL地址为/page/8/
    re_path(r'^page/(?P<pk>\d+)/$', views.page_detail, name='page_detail'),

]