import xadmin
from xadmin.plugins.auth import UserAdmin

from apps.users.models import UserInfo, VerifyCode


class UserInfoAdmin(UserAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']


xadmin.site.register(VerifyCode)
xadmin.site.unregister(UserInfo)
xadmin.site.register(UserInfo, UserInfoAdmin)
