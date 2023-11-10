from django.db import models


# Create your models here.

# 新闻类
class NewsInfo(models.Model):
    """
    定义新闻表
    """
    # 新闻标题
    title = models.CharField(max_length=50)

    # 新闻内容
    content = models.TextField()

    # 新闻创建时间
    new_date = models.DateTimeField()

    # 新闻阅读量
    new_read = models.IntegerField()
