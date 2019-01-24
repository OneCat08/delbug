from django.db import models
from tinymce.models import HTMLField

# Create your models here.
# 我的项目表
class Project(models.Model):
    name = models.CharField(max_length=100)  # 项目标题
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）
    all_bugs = models.IntegerField()  # 总bug条数
    active_bugs = models.IntegerField()  # 活跃的bug条数

    def __str__(self):
        return self.name

# 我的团队表
class Team(models.Model):
    Tname = models.CharField(max_length=100)  # 团队名称
    create_time = models.DateTimeField(auto_now=True)  # 创建时间(自动获取当前时间)
    number = models.IntegerField()  # 团队人数

    def __str__(self):
        return self.Tname

# 项目详情表
class Bug(models.Model):
    Pid = models.ForeignKey(Project, on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)  # 缺陷标题
    status = models.IntegerField()  # 缺陷状态
    degree = models.IntegerField()  # 严重程度
    priority = models.IntegerField()  # 优先级
    Dealing_people = models.CharField(max_length=15)  # 处理人
    create_time = models.DateTimeField(auto_now=True)  # 创建时间
    # description = RichTextUploadingField()  # 描述
    description = models.BinaryField()  # 描述

    def __str__(self):
        return self.name
