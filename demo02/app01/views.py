
from django.shortcuts import render, HttpResponse
from app01 import models


# Create your views here.


def index(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.FILES)
        # < QueryDict: {'username': ['sunzhen'], 'password': ['']} >
        # < MultiValueDict: {'file': [ < InMemoryUploadedFile: 2.j
        # pg(image / jpeg) >]} >
    return render(request, 'index.html')


import json


def ab_json(request):
    if request.is_ajax():
        # Content-Type: application/json
        print(request.body)
        #   {"username":"tom","age":18}
        # 针对json数据需要进行手动处理
        json_bytes = request.body
        # json.loads 括号内如果传入一个二进制格式的数据 则内部可以自动解码再反序列化
        json_dict = json.loads(json_bytes)
        print(json_dict, type(json_dict))
    #     {'username': 'tom', 'age': 18} <class 'dict'>
    return render(request, 'ab_json.html')


def ab_file(request):
    if request.is_ajax():
        if request.method == 'POST':
            print(request.POST)
            print(request.FILES)
            """
            <QueryDict: {'username': ['123'], 'password': ['123']}>
            <MultiValueDict: {'myfile': [<InMemoryUploadedFile: 2.jpg (image/jpeg)>]}>

            """
    return render(request, 'ab_file.html')


from django.http import JsonResponse
from django.core import serializers


def ab_ser(request):
    user_queryset = models.User.objects.all()
    # [{},{},{},{}]
    # user_list = []
    # for user_obj in user_queryset:
    #     tmp = {
    #         'pk': user_obj.pk,
    #         'username': user_obj.username,
    #         'age': user_obj.age,
    #         'gender': user_obj.get_gender_display()
    #     }
    #     user_list.append(tmp)
    # return JsonResponse(user_list, safe=False)
    # 序列化
    # serializers.serialize 方法第一个参数是返回数据的格式
    # 会自动的将数据变成json字符串 内部非常全面
    res = serializers.serialize('json', user_queryset)
    return HttpResponse(res)
    # return render(request, 'ab_ser.html', locals())


"""
[{"model": "app01.user", "pk": 1, "fields": {"username": "tim", "age": 18, "gender": 1}},
{"model": "app01.user", "pk": 2, "fields": {"username": "tom", "age": 19, "gender": 2}},
{"model": "app01.user", "pk": 3, "fields": {"username": "jim", "age": 20, "gender": 3}},
{"model": "app01.user", "pk": 4, "fields": {"username": "joy", "age": 21, "gender": 4}}]
利用序列化组建渲染数据写一个接口文档
"""


def user_list(request):
    user_queryset = models.User.objects.all()
    return render(request, 'user_list.html', locals())


import time


def delete_user(request):
    if request.is_ajax():
        if request.method == 'POST':
            back_dic = {'code': 1000, 'msg': ''}
            time.sleep(3)
            delete_id = request.POST.get('delete_id')
            models.User.objects.filter(pk=delete_id).delete()
            back_dic['msg'] = '数据已经删除，无法恢复'
            # 我们需要告诉前端操作的结果
            return JsonResponse(back_dic)


from utils.mypage import Pagination


def ab_pl(request):
    # 向book内插入10000条数据
    # for i in range(100):
    #     models.Book.objects.create(title='第%s本书' % i)
    # book_queryset = models.Book.objects.all()
    # 展示到前端页面上

    # 批量插入   bulk_create
    # book_list = []
    # for i in range(100):
    #     book_obj = models.Book(title='第%s本书' % i)
    #     book_list.append(book_obj)
    # models.Book.objects.bulk_create(book_list)

    # # 分页
    # book_list = models.Book.objects.all()
    #
    # # 分页的参数
    # # 想访问那一页
    # current_page = request.GET.get('page', 1)  # 如果获取不到当前页码，展示第一页
    # # 数据转换
    # try:
    #     current_page = int(current_page)
    # except Exception:
    #     current_page = 1
    # # 每页展示多少条
    # per_page = 10
    # # 起始位置
    # str_page = (current_page - 1) * per_page
    # # 终止位置
    # end_page = current_page * per_page
    # # 计算出到底需要多少页
    # all_count = book_list.count()
    # page_count, more = divmod(all_count, per_page)
    # if more:
    #     page_count += 1
    #
    # page_html = ''
    # gl_current_page = current_page
    # if current_page < 6:
    #     current_page = 6
    # for i in range(current_page - 5, current_page + 6):
    #     if gl_current_page == i:
    #         page_html += ' <li class="active"><a href="?page=%s">%s</a></li>' % (i, i)
    #     else:
    #         page_html += ' <li ><a href="?page=%s">%s</a></li>' % (i, i)
    # book_queryset = book_list[str_page: end_page]
    book_queryset = models.Book.objects.all()
    current_page = request.GET.get('page', 1)
    all_count = book_queryset.count()

    # 1.生成传值对象
    page_obj = Pagination(current_page=current_page, all_count=all_count)
    # 2.直接对总数据进行切片操作
    page_queryset = book_queryset[page_obj.start: page_obj.end]
    # 3.把page_queryset传递到页面，替换之前的 book_queryset
    return render(request, 'ab_pl.html', locals())
