from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

"""
视图函数定义的基本要求：
    1、视图函数必须定义一个参数（通过命名为request）
        request参数：用来接受客户端的请求信息
    2、视图函数的返回值必须是一个HttpResponse对象（或者HttpResponse子类对象）
"""


def index(request):
    content = '这是我们之间的名字'
    return HttpResponse(content)
