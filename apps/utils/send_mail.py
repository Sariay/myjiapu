import os
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


def send_email(email_name, verify_code):
    subject = "这是来自'家谱网'的注册确认邮件"

    text_content = '''感谢注册家谱网！\ 
                    如果您看到这条消息，说明您的邮箱服务器不提供HTML链接功能，请联系网站管理员！'''

    html_content = '''
                     <p>
                        感谢注册<a href="http://{}/verify/?verify_code={}" target=blank>家谱网</a>，请点击站点链接完成注册确认！
                     </p>
                     <br/>
                     <p>
                        此链接有效期为{}天！
                     </p>
                     '''.format('127.0.0.1:8000', verify_code, settings.EXPIRE_DAYS)

                    # TODO: 配置域名

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email_name])
    msg.attach_alternative(html_content, "text/html")
    msg.send()