from django.shortcuts import render, HttpResponse, redirect
from .models import NewsInfo

# Create your views here.

"""
视图函数定义的基本要求：
    1、视图函数必须定义一个参数（通过命名为request）
        request参数：用来接受客户端的请求信息
    2、视图函数的返回值必须是一个HttpResponse对象（或者HttpResponse子类对象）
    
视图使用的流程：
    1、在应用的views.py定义视图函数
    2、配置路由
    ·在项目目录的urls.py中关联应用下的urls.py
    ·在应用目录下定义一个urls.py文件（可以直接复制项目下的urls文件)
    ·配置具体的访问规则
    
模板的使用：
    1、在项目目录中创建一个templates文件夹
    2、在setting.py中TEMPLATES选项中配置项目模板的根目录
    'DIRS': [BASE_DIR / 'templates']
    3、在templates中创建和应用同名的文件夹
    4、在templates下应用同名的文件夹中创建html模板页面
    5、在views.py中定义视图函数 使用render函数返回函数模板页面
    6、配置配置路由规则
"""


def index(request):
    content = '''
        <html>
            <head>
                <title>你的名字</title>
            </head>
            <body>
                <h1>不知道你的名字</h1>
            </body>
        </html>
    '''
    return HttpResponse(content)


def newList(request):
    """返回新闻列表"""
    # 获取所有的新闻信息
    # select * from NewsInfo
    QuerySet = NewsInfo.objects.all()
    print(QuerySet)

    result = ''
    # 遍历所有的数据
    for item in QuerySet:
        # 获取新闻的标题
        title = f'<h1>{item.title}</h1>'

        result += title

    return HttpResponse(result)


def newListTemplate(request):
    """在视图中使用模板"""
    """
        1、通过模型去查询数据
        2、
    """
    dataSet = NewsInfo.objects.all()

    # 获取查询到的第一条新闻信息
    item = dataSet[1]
    info = {
        'title': item.title,
        'content': item.content,
        'new_date': item.new_date,
        'new_read': item.new_read,
    }
    """
    render 渲染模板所需的三个参数
    1、请求对象 request
    2、模板文件路径
    3、渲染到模板中的数据 字典格式 使用方式是插值表达式{{property}}
    """
    return render(request, 'news/list.html', info)
