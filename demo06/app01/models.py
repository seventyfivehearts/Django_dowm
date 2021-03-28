from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.


# 扩展表的几种方式
# 第一种: 一对一关系 不推荐
# class UserDetail(models.Model):
#     phone = models.BigIntegerField()
#     user = models.OneToOneField(to='User')

# 第二种 利用面向对象的继承
class UserInfo(AbstractUser):
    """
    这里进行的操作
        如果执行了AbstractUser
        那么在执行数据库迁移命令的时候，auth_user表就不会被创建出来
        而UserInfo 表会出现在auth_user所有字段，并且加上自己扩展的字段

        前提  1.在继承AbstractUser之前没有执行过数据库迁移命令(没有把auth_user表床架出来)
             2.继承的类里里面不要覆盖abstractuser里面的字段名
             3.需要在配置文件中告诉django 使用UserInfo替换auth_user
             AUTH_USER_MODEL = ‘app01.UserInfo’,(应用名.表名)
    """
    phone = models.BigIntegerField()
