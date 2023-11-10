from django.contrib import admin
from .models import NewsInfo


# Register your models here.
# 注册模型类  直接使用后台默认管理界面
# admin.site.register(NewsInfo)


# 自定义管理页面
class NewsInfoAdmin(admin.ModelAdmin):
    """显示自定义NewsInfo字段数据"""
    list_display = ['id', 'title', 'content', 'new_date', 'new_read']
    # 分页功能
    list_per_page = 2


admin.site.register(NewsInfo, NewsInfoAdmin)

"""
list_display = ("__str__",) //管理页显示哪些字段，例如("id", "fullname")
list_display_links = ()     //哪些字段带管理链接，例如("fullname", "firstname")
list_filter = ()            //过滤器，用来显示修改过的项目
list_select_related = False //检索管理更改列表页面上的对象列表。这可以为您节省大量数据库查询
list_per_page = 100         //分页显示，每页显示条目的数量
list_max_show_all = 200     //显示全部的最大数量
list_editable = ()          //括号项中的内容在列表页可以直接编辑
search_fields = ()          //列表页中放大镜图标可以搜索的字段定义
search_help_text = None     //为搜索添加说明内容
date_hierarchy = None       //根据日期层级筛选字段内容
save_as = False             //是否显示数据另存为表中新行
save_as_continue = True     //是否显示保存并继续
save_on_top = False         //是否以更详细的编辑页面显示，包括删除等按钮
paginator = Paginator       //更详细的分页操作，可自定义更多分页功能
preserve_filters = True     //True在编辑后显示原有过滤状态，False即相反
inlines = ()                //配合自定义类，显示更多更详细的编辑内容
"""
