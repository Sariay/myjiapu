import xadmin

from xadmin.layout import Fieldset, Main, Side, Row
from apps.history.models import LineageTree, HusbandToWife, GravesMainMap, GravesSupplementMap, GeoPosition
from apps.users.models import UserInfo, VerifyCode


class GlobalSettings(object):
    site_title = "后台系统"
    site_footer = "家谱管理&编辑系统"
    # menu_style = "accordion"
    global_search_models = [LineageTree, HusbandToWife, GeoPosition, GravesMainMap, GravesSupplementMap, UserInfo, VerifyCode]
    global_models_icon = {
        LineageTree: "fa fa-sitemap",
        HusbandToWife: "fa fa-exchange",
        GeoPosition: "fa fa-map-marker",
        GravesMainMap: "fa fa-globe",
        GravesSupplementMap: "fa fa-globe",
        UserInfo: "fa fa-user-plus",
        VerifyCode: "fa fa-check-square-o"
    }


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)