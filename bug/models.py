from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

# 我的团队表
class Team(models.Model):
    Tname = models.CharField(max_length=100)  # 团队名称
    create_time = models.DateTimeField(auto_now=True)  # 创建时间(自动获取当前时间)
    number = models.IntegerField()  # 团队人数
    Team_peo = models.CharField(max_length=10000)  # 团队成员ID

    def __str__(self):
        return self.Tname

# 我的项目表
class Project(models.Model):
    name = models.CharField(max_length=100)  # 项目标题
    create_time = models.DateTimeField(auto_now=True)  # 创建时间（自动获取当前时间）
    all_bugs = models.IntegerField()  # 总bug条数
    active_bugs = models.IntegerField()  # 活跃的bug条数
    Tid = models.ForeignKey(Team, on_delete=models.DO_NOTHING,)  # 所属的团队ID
    Project_peo = models.CharField(max_length=1000)  # 项目成员ID 1,2,3等

    def __str__(self):
        return self.name

# 项目详情表
class Bug(models.Model):
    status_list = (
        (1, '待处理'),
        (2, '待审核'),
        (3, '已修复'),
        (4, '已拒绝')
    )
    degree_list = (
        (1, '致命'),
        (2, '严重'),
        (3, '较重'),
        (4, '一般'),
        (5, '建议')
    )
    priority_list = (
        (1, '马上解决'),
        (2, '急需解决'),
        (3, '高度重视'),
        (4, '正常处理'),
        (5, '低优先级')
    )

    Pid = models.ForeignKey(Project, on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)  # 缺陷标题
    status = models.IntegerField(choices=status_list)  # 缺陷状态
    degree = models.IntegerField(choices=degree_list)  # 严重程度
    priority = models.IntegerField(choices=priority_list)  # 优先级
    create_peo = models.IntegerField()  # 创建人
    Dealing_people = models.IntegerField()  # 处理人
    create_time = models.DateTimeField(auto_now=True)  # 创建时间
    close_time = models.DateTimeField()  # 关闭时间
    # description = RichTextUploadingField()  # 描述
    description = models.BinaryField()  # 描述

    def __str__(self):
        return self.name

# 用户扩展
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
