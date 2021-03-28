from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

"""
用auth模块需要用全套, 不能单点
"""


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 去用户表中校验数据
        # 1.表如何获取
        # 2.密码如何比对
        user_obj = auth.authenticate(request, username=username, password=password)
        # print(user_obj)  # 用户对象      数据不符合则返回none
        # print(user_obj.username)
        # print(user_obj.password)
        # 判断当前用户是否存在
        if user_obj:
            # 保存用户状态
            auth.login(request, user_obj)  # 类似于request.session[key]=user_obj
            # def login(request, user, backend=None):
            # 只要执行了该方法，则可以在任何地方都拿到request.user 获取到当前用户登录对象
            return redirect('/home/')
        """
        jrsmith
        pbkdf2_sha256$36000$BOP3ED4NVaZs$DS4AkxAfvcskO4muRXHgHNJGvmghN0j/VQjjOfHV9LA=
        """
        """
        def authenticate(request=None, **credentials):
        1.自动查找auth标签
        2.自动给密码加密进行比对
            注意： 该方法需要一次性传入username password 两个参数进行校验， 不能只传用户名
        """
    return render(request, 'login.html')


from django.contrib.auth.decorators import login_required

# auth 封装的 装饰器 判断用户是否登录
# @login_required(login_url='/login/')    # 局部配置，用户没有登录跳转到login_url后面指定的网址

# 优先级局部 > 全局


"""
全局的好处，无需重复代码 但是跳转的页面单一
局部的好处在于可以使用不同的视图函数使得用户在没有登录的界面可以跳转到多个界面
"""


@login_required  # 全局配置
def home(request):
    print(request.user)  # jrsmith 用户对象
    # 判断当前用户是否登录
    print(request.user.is_authenticated())  # True
    return HttpResponse('home')


# 用户修改密码
@login_required
def set_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        if new_password == confirm_password:
            # 校验老密码对不对
            is_right = request.user.check_password(old_password)  # 自动加密密码进行比对
            if is_right:
                # 修改密码
                request.user.set_password(new_password)  # 这一步仅仅是修改对象的属性
                request.user.save()  # 这一步是真正的操作数据库
        return redirect('/login/')

    return render(request, 'set_password.html', locals())


@login_required
def logout(request):
    auth.logout(request)  # 类似于request.session.flush()
    return redirect(request, 'login.html')


from django.contrib.auth.models import User


# 注册功能
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 操作auth表写入数据
        # User.objects.create(username=username, password=password) # 写入数据不能用create
        # 创建普通用户
        User.objects.create_user(username=username, password=password)
        # 创建超级用户
        # User.objects.create_superuser(username=username, password=password)

    return render(request, 'register.html')


