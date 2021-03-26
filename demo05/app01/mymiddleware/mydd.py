from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print('我是第一个自定义的方法process_request')
        # return HttpResponse('我是第一个自定义的方法process_request返回的数据')

    def process_view(self, request, view_name, *args, **kwargs):
        print(view_name, args, kwargs)

    def process_response(self, request, response):
        print('我是第一个定义的process_response方法')
        return response

    def process_template_response(self, request, response):
        print('我是第一个自定义的process_template_response方法')
        return response

    def process_exception(self, request, exception):
        print('我是第一个自定义的process_exception方法')
        print(exception)