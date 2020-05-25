from django import forms
from captcha.fields import CaptchaField

from apps.users.models import UserInfo


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=150)
    password = forms.CharField(required=True, min_length=8)


class SignupGetVerifyCodeForm(forms.Form):
    captcha = CaptchaField()


class SignupForm(forms.Form):
    username = forms.CharField(required=True, min_length=6)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=8)
    password_confirm = forms.CharField(required=True, min_length=8)
    captcha = CaptchaField()

    def clean_password(self):
        pass_word = self.data.get("password")
        pass_word_confirm = self.data.get("password_confirm")
        if pass_word != pass_word_confirm:
            raise forms.ValidationError("两次输入的密码不同！")

    def clean_username(self):
        user_name = self.data.get("username")
        # 验证邮箱是否已经注册
        users = UserInfo.objects.filter(username=user_name)
        if users:
            raise forms.ValidationError("该用户名已被注册")
        return user_name

    def clean_email(self):
        email = self.data.get("email")
        # 验证邮箱是否已经注册
        users = UserInfo.objects.filter(email=email)
        if users:
            raise forms.ValidationError("该邮箱已被注册")
        return email

    # TODO: 邮箱验证码的的生成及发送
    # def clean_code(self):
    #     mobile = self.data.get("mobile")
    #     code = self.data.get("code")
    #     r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, charset="utf8", decode_responses=True)
    #     redis_code = r.get(str(mobile))
    #     if code != redis_code:
    #         raise forms.ValidationError("验证码不正确")
    #     return code