from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        abstract = True


class UserInfo(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="昵称", blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="地址", blank=True)
    mobile = models.CharField(max_length=11, verbose_name="手机号码", blank=True)
    has_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
        ordering = ["-date_joined"]

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username


class VerifyCode(BaseModel):
    user = models.OneToOneField('UserInfo', on_delete=models.CASCADE)
    verify_code = models.CharField(max_length=256)

    def __str__(self):
        return self.user.username + ": " + self.verify_code

    class Meta:
        verbose_name = "确认码"
        verbose_name_plural = verbose_name
        ordering = ["-add_time"]


