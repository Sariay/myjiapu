import datetime

from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import models
# Create your views here.

from django.conf import settings
from apps.users.forms import LoginForm, SignupGetVerifyCodeForm, SignupForm
from apps.users.models import UserInfo, VerifyCode
from apps.utils.hash_code import hash_code
from apps.utils.send_mail import send_email


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    # def post(self,   request, *args, **kwargs):
    #     return render(request, 'index.html')
    # TODO: 主页是否存在提交表单的操作POST

#登录
class LoginView(View):
    def get(self, request, *args, **kwargs):
        verify_code_form = SignupGetVerifyCodeForm()
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        next = request.GET.get("redirect_to", '')
        return render(request, "login.html", {
            "verify_code_form": verify_code_form,
            "next": next
        })

    def post(self,   request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        verify_code_form = SignupGetVerifyCodeForm()

        if request.user.is_authenticated:
            next = request.GET.get("redirect_to", '')
            if next:
                return HttpResponseRedirect(next)
            return HttpResponseRedirect(reverse("home"))

        if login_form.is_valid():
            user_name = login_form.cleaned_data["username"]
            pass_word = login_form.cleaned_data["password"]

            #通过用户名和密码查询用户是否存在
            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                # 查询到用户
                if not user.has_verified:
                    return render(request, "login.html", {
                        "msg": "该用户还未经过邮件验证！",
                        "login_form": login_form,
                        "verify_code_form": verify_code_form
                    })

                login(request, user)
                next = request.GET.get("redirect_to", '')
                if next:
                    return HttpResponseRedirect(next)
                return HttpResponseRedirect(reverse("home"))
            else:
                return render(request, "login.html", {
                    "msg": "用户名或密码错误",
                    "login_form": login_form,
                    "verify_code_form": verify_code_form
                })
        else:
            return render(request, "login.html", {
                "login_form": login_form,
                "verify_code_form": verify_code_form
            })


#登出
class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("home"))


#注册
class SignupView(View):
    def get(self, request, *args, **kwargs):
        verify_code_form = SignupGetVerifyCodeForm()
        return render(request, 'signup.html', {
            "verify_code_form": verify_code_form,
        })

    def post(self, request, *args, **kwargs):
        signup_form = SignupForm(request.POST)
        verify_code_form = SignupGetVerifyCodeForm()
        # msg = "请检查填写的内容！"
        if signup_form.is_valid():
            user_name = signup_form.cleaned_data["username"]
            email = signup_form.cleaned_data["email"]
            pass_word = signup_form.cleaned_data["password"]

            # 新建一个用户
            user = UserInfo(username=user_name)
            user.email = email
            # hash加密密码，写密文密码到数据表
            user.set_password(pass_word)
            # 未激活
            user.is_active = False
            # 不可登录管理系统
            user.is_staff = False
            user.save()

            now_time = datetime.datetime.now().strftime("%Y-%m-%d  %H%M%S")
            verify_code = hash_code(user.username, now_time)

            verify_code_user = VerifyCode(verify_code=verify_code, user=user)

            verify_code_user.save()

            email_verify_code = verify_code
            print(email_verify_code)

            send_email(email, email_verify_code)

            login(request, user)
            return HttpResponseRedirect(reverse("verify"))

        #表单验证无效
        else:
            return render(request, 'signup.html', {
                "verify_code_form": verify_code_form,
                "signup_form": signup_form
            })


class SignupVerifyView(View):
    def get(self, request, *args, **kwargs):
        verify_code = request.GET.get('verify_code', None)
        message = ''

        try:
            # verify_user = models.VerifyCode.objects.get(verify_code=verify_code)
            verify_user = VerifyCode.objects.get(verify_code=verify_code)
            # TODO: 直接相应表查询
        except:
            message = '请通过邮箱链接进行账户激活!'
            return render(request, 'signup_verify.html', locals())

        add_time = verify_user.add_time
        now_time = datetime.datetime.now()

        if now_time > add_time + datetime.timedelta(settings.EXPIRE_DAYS):
            verify_user.user.delete()
            message = '您的邮件已经过期！请重新注册!'
            return render(request, 'signup_verify.html', locals())
        else:
            verify_user.user.has_verified = True
            verify_user.user.is_active = True
            verify_user.user.save()
            verify_user.delete()
            message = '感谢确认，请使用账户登录！'
            return render(request, 'signup_verify.html', locals())

        return render(request, 'signup.html')