import xadmin

from apps.history.models import GeoPosition, LineageTree, HusbandToWife, GravesMainMap, GravesSupplementMap


class GeoPositionAdmin(object):
    list_display = ['migrate_order', 'from_address', 'to_address', 'to_altitude', 'to_longtitude', 'introduction']
    search_fields = ['migrate_order', 'from_address', 'to_address', 'to_altitude', 'to_longtitude', 'introduction']
    list_filter = ['migrate_order', 'from_address', 'to_address', 'to_altitude', 'to_longtitude', 'introduction']
    list_editable = ['migrate_order', 'from_address', 'to_address', 'to_altitude', 'to_longtitude', 'introduction']


class LineageTreeAdmin(object):
    list_display = ['lineage_area', 'lineage_level', 'name', 'father', 'gender', 'introduction', 'untested_info']
    search_fields = ['lineage_area', 'lineage_level', 'name', 'father', 'gender', 'introduction', 'untested_info']
    list_filter = ['lineage_area', 'lineage_level', 'name', 'father', 'gender', 'introduction', 'untested_info']
    list_editable = ['lineage_area', 'lineage_level', 'name', 'father', 'gender', 'introduction', 'untested_info']


class HusbandToWifeAdmin(object):
    list_display = ['marriage_to', 'name', 'belong_to_who', 'father','gender', 'introduction', 'untested_info']
    search_fields = ['marriage_to', 'name', 'belong_to_who', 'father','gender', 'introduction', 'untested_info', 'lineage_area', 'lineage_level']
    list_filter = ['marriage_to', 'name', 'belong_to_who', 'father','gender', 'introduction', 'untested_info', 'lineage_area', 'lineage_level']
    list_editable = ['marriage_to', 'name', 'belong_to_who', 'father','gender', 'introduction', 'untested_info', 'lineage_area', 'lineage_level']


class GravesMainMapAdmin(object):
    list_display = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']
    search_fields = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']
    list_filter = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']
    list_editable = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']



class GravesSupplementMapAdmin(object):
    list_display = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']
    search_fields = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']
    list_filter = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']
    list_editable = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']


class Gr(object):
    list_display = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']
    search_fields = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']
    list_filter = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']
    list_editable = ['lineage_area', 'belong_to_user', 'grave_address', 'introduction', 'altitude', 'longtitude']


xadmin.site.register(GeoPosition, GeoPositionAdmin)
xadmin.site.register(LineageTree, LineageTreeAdmin)
xadmin.site.register(HusbandToWife, HusbandToWifeAdmin)
xadmin.site.register(GravesMainMap, GravesMainMapAdmin)
xadmin.site.register(GravesSupplementMap, GravesSupplementMapAdmin)


