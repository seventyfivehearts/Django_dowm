from django.db import models


# Create your models here.

# class Book(models.Model):
#     name = models.CharField(max_length=32)
#     #  through='Book2Author' 这个参数 通过自己创建的表创建的关系的
#     authors = models.ManyToManyField(to='Author',
#                                      through='Book2Author',
#                                      through_fields=('book', 'author')
#                                      )
#
#
# """
# through_fields
# 先后顺序
#     判断的本质：
#         通过第三张表查询对应的表，需要用到那个字段就将那个字段放在前面
#         简化判断
#             当前表是谁就放在前面
# """
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=32)
#
#
# class Book2Author(models.Model):
#     book = models.ForeignKey(to='Book')
#     author = models.ForeignKey(to='Author')
#
#
# class User(models.Model):
#     username = models.CharField(max_length=12)
#     age = models.IntegerField()
#     gender_choices = (
#         (1, 'man'),
#         (2, 'woman'),
#         (3, 'other'),
#     )
#     # IntegerField 与 元组中的有关
#     gender = models.IntegerField(choices=gender_choices)
#     """
#     gender中存的是数字，如果元组中存在的数字与元组中的数字相对应，那么会将数字后面的值获取的到
#     """
#     score_choices = (
#         ('A', '优秀'),
#         ('B', '良好'),
#         ('C', '及格'),
#         ('D', '不及格'),
#     )
#     # 这里需要注意 要保证字段列举的类型与元祖的第一个数据一样
#     score = models.CharField(choices=score_choices, null=True)
