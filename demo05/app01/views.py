from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator
# Create your views here.
from django.views.decorators.csrf import csrf_protect, csrf_exempt

"""
csrf_protect    需要校验
    针对CBV装饰器 三种方式都有效
csrf_exempt     不要校验
    针对CBV装饰器 只有给dispatch加才有效
"""


def index(request):
    print('视图函数index')

    obj = HttpResponse('index')

    def render():
        print('内部的render')
        return HttpResponse('ok_ok')

    obj.render = render
    return obj


# @csrf_protect
# @csrf_exempt
def transfer(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        target = request.POST.get('target')
        money = request.POST.get('money')
        print('%s给%s转了%s元' % (username, target, money))
    return render(request, 'transfer.html')


from django.views import View


# @method_decorator(csrf_protect, name='post')  # 第二种方式 csrf_protect可以
class Mycsrf(View):
    # @method_decorator(csrf_protect) #  第三种方式 csrf_protect可以
    @method_decorator(csrf_exempt())  # 只有第三种方式 csrf_protect可以
    def dispatch(self, request, *args, **kwargs):
        return super(Mycsrf, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse('get')

    # @method_decorator(csrf_protect)  # 第一种方式 csrf_protect可以
    def post(self, request):
        return HttpResponse('post')
