from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

# 校验用户是否登录的装饰器
def login_auth(func):
    def inner(request, *args, **kwargs):
        target_url = request.get_full_path()  # 获取到用户上一次访问的url
        if request.COOKIES.get('username'):
            res = func(request, *args, **kwargs)
            return res
        else:
            return redirect('/login/?next=%s' % target_url)

    return inner


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'tom' and password == '123':
            # 获取用户上一次输入的url(GET请求)
            target_url = request.GET.get('next')  # 这个结果可能是None
            if target_url:
                obj = redirect(target_url)
            else:
                # 保存用户登录状态
                obj = redirect('/home/')
            # 让浏览器记录cookie数据
            obj.set_cookie('username', 'tom', max_age=3, expires=3)
            # 设置超时时间长3秒(用户信息保存的时间)
            return obj
    return render(request, 'login.html')


@login_auth
def home(request):
    # 获取cookie信息判断是否登录
    # if request.COOKIES.get('username') == 'tom':
    #     return HttpResponse('这是登录之后能访问的页面')
    # else:
    #     redirect('/login/')
    return HttpResponse('这是登录之后能访问home的页面')


@login_auth
def index(request):
    # 获取cookie信息判断是否登录
    # if request.COOKIES.get('username') == 'tom':
    #     return HttpResponse('这是登录之后能访问的页面')
    # else:
    #     redirect('/login/')
    return HttpResponse('这是登录之后能访问index的页面')


@login_auth
def func1(request):
    # 获取cookie信息判断是否登录
    # if request.COOKIES.get('username') == 'tom':
    #     return HttpResponse('这是登录之后能访问funcs的页面')
    # else:
    #     redirect('/login/')
    return HttpResponse('这是登录之后能访问的页面')


@login_auth
def logout(request):
    obj = redirect('/login/')
    obj.delete_cookie('username')
    return obj


def set_session(request):
    request.session['hobby'] = 'sleep'
    """
    内部发生的事情
    1.Django中产生一个随机字符串
    2.django内部自动将随机字符串和对应的数据存放在session表中
        2.1先在内存中产生缓存
        2.2响应结果在中间件的时候才真正操作数据库
    3.将产生的随机字符串返回给客户端保存
    """
    return HttpResponse('set_session')


def get_session(request):
    print(request.session.get('hobby'))
    """
    内部发生的事
    1.获取浏览器请求产生的随机字符串 session_id
    2.拿着session_id 去django_session表中查找数据
    3.如果存在，则把数据以字典的形式封装在request.session中
        如果比对不上则返回的是None
    """
    return HttpResponse('get_session')



from django.views import View
from django.utils.decorators import method_decorator
"""
cbv 中django 不建议加装饰器
无论装饰器是否能正常给你， 都不建议加
 语法 @method_decorator(login_auth)
"""


#  方式2 指名道姓的装 可以指定多个, 针对不同的方法可以装不同的装饰器
@method_decorator(login_auth, name='get')
@method_decorator(login_auth, name='post')
class MyLogin(View):
    @method_decorator(login_auth)  # 方式3 直接作用与当前类里所有的方法
    def dispatch(self, request, *args, **kwargs):
        pass
    # @method_decorator(login_auth) # 方式1
    def get(self):
        return HttpResponse('get请求')

    # @method_decorator(login_auth)
    def post(self):
        return HttpResponse('post请求')





