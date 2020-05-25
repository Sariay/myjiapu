from django.db import models

from apps.users.models import BaseModel

# Create your models here.
GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)

MIGRATE_AREA_CHOICES = (
    ("unknow", "未知"),
    ("xuan_wei", "宣威县"),
    ("fang_zhu", "放珠镇"),
    ("mai_bai", "马摆乡"),
    ("guan_zhai", "马摆官寨"),
    ("hou_cao", "马摆后槽"),
    ("da_fang", "大方县"),
    ("dong_di", "董地乡田坝寨"),
    ("zhi_jin", "织金县"),
)

MIGRATE_ORDER_CHOICES = (
    ("order1", "第一次迁徙"),
    ("order2", "第二次迁徙"),
    ("order3", "第三次迁徙"),
    ("order4", "第四次迁徙"),
    ("order5", "第五次迁徙"),
    ("order6", "第六次迁徙"),
    ("order7", "第七次迁徙"),
)

LINEAGE_AREA_CHOICES = (
    ("m_zhangfang", "马摆长房"),
    ("m_erfang", "马摆二房"),
    ("m_yaofang", "马摆幺房"),
    ("b_fangzhu", "毕节放珠支系"),
)

LINEAGE_LEVEL_CHOICES = (
    ("order1", "一世"),
    ("order2", "二世"),
    ("order3", "三世"),
    ("order4", "四世"),
    ("order5", "五世"),
    ("order6", "六世"),
    ("order7", "七世"),
    ("order8", "八世"),
    ("order9", "九世"),
    ("order10", "十世"),
    ("order11", "十一世"),
    ("order12", "十二世"),
)

MARRIAGE_CHOICES = (
    ("marriage_in", "娶入"),
    ("marriage_out", "嫁出"),
)

# 迁徙图数据表
class GeoPosition(BaseModel):
    migrate_order = models.CharField(choices=MIGRATE_ORDER_CHOICES, verbose_name="迁徙序列", max_length=50, default='')
    from_address = models.CharField(choices=MIGRATE_AREA_CHOICES, verbose_name="迁出地", max_length=50, default='')
    to_address = models.CharField(choices=MIGRATE_AREA_CHOICES, verbose_name="迁入地", max_length=50, default='')
    to_altitude = models.CharField(max_length=100, verbose_name="迁入地经度", default='')
    to_longtitude = models.CharField(max_length=100, verbose_name="迁入地纬度", default='')
    now_address = models.CharField(choices=MIGRATE_AREA_CHOICES, verbose_name="现居地", max_length=50, default='')
    now_address_particular = models.CharField(max_length=100, verbose_name="具体地名", default='')
    introduction = models.CharField(max_length=1000, verbose_name="简介", blank=True)

    class Meta:
        verbose_name = "迁徙地标"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.migrate_order


# 世系图数据表
class LineageTree(BaseModel):
    lineage_area = models.CharField(choices=LINEAGE_AREA_CHOICES, verbose_name="所属世系", max_length=50, default='')
    lineage_level = models.CharField(choices=LINEAGE_LEVEL_CHOICES, verbose_name="世系代数", max_length=50, default='')
    name = models.CharField(max_length=50, verbose_name="姓名")
    father = models.CharField(max_length=50, verbose_name="父亲姓名")
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    introduction = models.CharField(max_length=1000, verbose_name="简介", blank=True)
    untested_info = models.CharField(max_length=1000, verbose_name="待考证信息", blank=True)

    class Meta:
        verbose_name = "世系信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 世系图数据表
class HusbandToWife(BaseModel):
    marriage_to = models.CharField(choices=MARRIAGE_CHOICES, verbose_name="嫁娶", max_length=50, default='')
    name = models.CharField(max_length=50, verbose_name="姓名")
    belong_to_who = models.OneToOneField('LineageTree', on_delete=models.CASCADE, verbose_name="配偶姓名", default='')
    father = models.CharField(max_length=50, verbose_name="父亲姓名")
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6)
    lineage_area = models.CharField(choices=LINEAGE_AREA_CHOICES, verbose_name="所属世系", max_length=50, default='')
    lineage_level = models.CharField(choices=LINEAGE_LEVEL_CHOICES, verbose_name="世系代数", max_length=50, default='')
    introduction = models.CharField(max_length=1000, verbose_name="简介", blank=True)
    untested_info = models.CharField(max_length=1000, verbose_name="待考证信息", blank=True)

    class Meta:
        verbose_name = "娶入嫁出"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GravesBaseModel(BaseModel):
    lineage_area = models.CharField(choices=LINEAGE_AREA_CHOICES, verbose_name="所属世系", max_length=50, default='')
    grave_address = models.CharField(max_length=50, verbose_name="墓址")
    introduction = models.CharField(max_length=1000, verbose_name="简介")
    altitude = models.CharField(max_length=1000, verbose_name="经度")
    longtitude = models.CharField(max_length=1000, verbose_name="纬度")


# 坟茔图数据表
class GravesMainMap(GravesBaseModel):
    belong_to_user = models.OneToOneField('LineageTree', on_delete=models.CASCADE, verbose_name="世系姓名", default='')

    class Meta:
        verbose_name = "坟茔信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.belong_to_user.name


# 坟茔图数据表
class GravesSupplementMap(GravesBaseModel):
    belong_to_user = models.OneToOneField('HusbandToWife', on_delete=models.CASCADE, verbose_name="世系姓名", default='')

    class Meta:
        verbose_name = "坟茔补充"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.belong_to_user.name


# 世系图：
# 1.本家父及其子女一张表。
# 2.妻及婿一张表。
# 3.1和2，一对一关系。
#
# 坟茔图
# 1.本家父及其子女一张表。 女一般不录信息 （一一对应世系图1）
# 2.妻及婿一张表。 婿不录入信息 （一一对应世系图2）
# 3.1和2，一对一关系。