from django.contrib import admin
from bug.models import Project, Team, Bug
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'create_time']
    search_fields = ['name'] # 搜索栏

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'Tname', 'create_time']
    search_fields = ['Tname']

class BugAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'Dealing_people']
    search_fields = ['id']

admin.site.register(Project, ProjectAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Bug, BugAdmin)
