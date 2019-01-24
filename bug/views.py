from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from bug.models import Project, Team, Bug
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/my_projects/')
            return response
        else:
            return render(request, 'index.html', {'error': '用户名或密码错误'})

# 我的项目管理
@login_required
def my_projects(request):
    project_list = Project.objects.all()
    username = request.session.get('user', '')
    paginator = Paginator(project_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页数据
        contacts = paginator.page(paginator.num_pages)
    return render(request,'my_projects.html', {'user': username,
                                               'projects': contacts})

# 我的项目名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    project_list = Project.objects.filter(name__contains=search_name)
    paginator = Paginator(project_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'my_projects.html', {'user': username,
                                                'projects': contacts})

# 我的团队管理
@login_required
def my_teams(request):
    username = request.session.get('user', '')
    team_list = Team.objects.all()
    paginator = Paginator(team_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'my_team.html', {'user': username,
                                            'teams': contacts})

# 项目详情页管理
@login_required
def project_details(request, pid):
    username = request.session.get('user', '')
    project = get_object_or_404(Project, id=pid)
    bug_list = Bug.objects.all()
    paginator = Paginator(bug_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'project_details.html', {'user': username,
                                                    'project': project,
                                                    'bugs': contacts})
# 项目详情缺陷id搜索
@login_required
def search_bugs(request):
    username = request.session.get('user', '')
    search_id = request.GET.get('id', '')
    bug_list = Bug.objects.filter(id__iexact=search_id)
    paginator = Paginator(bug_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围内，取最后一页数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'project_details.html', {'user': username,
                                                    'bugs': contacts})

# 创建缺陷页面
@login_required
def create_bug(request, pid):
    username = request.session.get('user', '')
    project = get_object_or_404(Project, id=pid)
    return render(request, 'create_bug.html', {'user': username,
                                               'project': project})

# 新建缺陷提交动作
def create_action(request, pid):
    if request.method == 'POST':
        pid = request.POST.get('pid', '')
        name = request.POST.get('name', '')
        degree = request.POST.get('degree', '')  # 严重程度
        priority = request.POST.get('priority', '')  # 优先级
        Dealing_people = request.POST.get('Dealing_people', '')
        content = request.POST.get('content', '')
        con = content.encode('utf-8')
        if name == '':
            return render(request, 'create_bug.html', {'error1': '标题不能为空'})
        else:
            bug = Bug(name=name, status=1, degree=degree, priority=priority,
                      Dealing_people=Dealing_people, description=con, Pid=pid)
            # 写入数据库
            bug.save()
            response = HttpResponseRedirect('/project_details/')
            return response
