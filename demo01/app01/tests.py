from django.test import TestCase

# Create your tests here.
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo01.settings")
    import django
    django.setup()

    from app01 import models

    # 存
    # models.User.objects.create(username='tom', age=19, gender=1)
    # models.User.objects.create(username='jim', age=20, gender=2)
    # models.User.objects.create(username='joy', age=21, gender=3)
    # 存的时候没有 列举的数字也可存进去(范围按照字段类型决定)
    # models.User.objects.create(username='tim', age=22, gender=4)

    # 取
    # 这种方法只能取到gender的数字
    # user_obj = models.User.objects.filter(pk=1).first()
    # print(user_obj.gender)
    # 只要是choices参数的字段，如果你想要获取到对应的信息， 固定写法 get_字段名_display()
    # get_gender_display()
    # 如果该方法对应的没有返回值 则字段是什么展示什么  4
    user_obj = models.User.objects.filter(pk=4).first()
    print(user_obj.get_gender_display())
