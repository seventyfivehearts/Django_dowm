from django.shortcuts import render, HttpResponse
from django import forms
from django.core.validators import RegexValidator


# Create your views here.


def ab_form(request):
    back_dic = {'username': '', 'password': ''}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if '测试' in username:
            back_dic['username'] = '测试名字不符合要求'
        if len(password) < 3:
            back_dic['password'] = '密码长度小于3'
    #         把当前的数据传递进来

    return render(request, 'ab_form.html', locals())


class MyForm(forms.Form):
    # username最短3位 最长八位
    username = forms.CharField(min_length=3, max_length=8, label='用户名：', initial='tom',
                               error_messages={
                                   'min_length': '用户名最少1位',
                                   'max_length': '用户名最多3位',
                                   'required': '用户名不能为空',
                               },
                               widget=forms.widgets.PasswordInput(attrs={'class': 'form-control c1 c2'})
                               )
    password = forms.CharField(min_length=3, max_length=8)
    confirm_password = forms.CharField(min_length=3, max_length=8)
    # 邮箱必须满足邮箱格式
    email = forms.EmailField()

    phone = forms.CharField(
        validators=[
            RegexValidator(r'^[0-9]+$', '请输入数字'),
            RegexValidator(r'^159[0-9]+$', '数字必须以159开头')
        ]
    )

    # 单选 radio
    gender = forms.fields.ChoiceField(
        choices=((1, "男"), (2, "女"), (3, "保密")),
        label="性别",
        initial=3,
        widget=forms.widgets.RadioSelect()
    )

    # 单选select
    hobby1 = forms.ChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )
    # 多选 selectMultiple
    hobby2 = forms.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.SelectMultiple()
    )

    # 单选checkbox
    keep = forms.ChoiceField(
        label="是否记住密码",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )

    # 多选checkBox
    hobby3 = forms.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.CheckboxSelectMultiple()
    )

    # 钩子函数
    # 局部钩子
    def clean_username(self):
        # 获取用户名
        username = self.cleaned_data.get('username')
        # 把错误信息展示到前端
        if '666' in username:
            self.add_error('username', '用户名中不能含有666')
        # 将钩子函数勾出的数据返回
        return username

    # 全局钩子
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if not confirm_password == password:
            self.add_error('confirm_password')
        return self.cleaned_data


def index(request):
    # form表单使用步骤
    # 1.先产生一个空对象
    form_obj = MyForm()
    if request.method == 'POST':
        """
        校验数据构造成字典的格式传入
        request.POST可以看做是一个字典
        """
        form_obj = MyForm(request.POST)
        if form_obj.is_valid():
            return HttpResponse('OK')
    # 2.直接将空对象传递给html页面
    return render(request, 'index.html', locals())
