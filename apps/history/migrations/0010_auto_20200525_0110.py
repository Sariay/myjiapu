# Generated by Django 2.2 on 2020-05-25 01:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0009_husbandtowife_marriage_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='GravesBaseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('lineage_area', models.CharField(choices=[('m_zhangfang', '马摆长房'), ('m_erfang', '马摆二房'), ('m_yaofang', '马摆幺房'), ('b_fangzhu', '毕节放珠支系')], default='', max_length=50, verbose_name='所属世系')),
                ('grave_address', models.CharField(max_length=50, verbose_name='墓址')),
                ('introduction', models.CharField(max_length=1000, verbose_name='简介')),
                ('altitude', models.CharField(max_length=1000, verbose_name='经度')),
                ('longtitude', models.CharField(max_length=1000, verbose_name='纬度')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GravesMainMap',
            fields=[
                ('gravesbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='history.GravesBaseModel')),
                ('belong_to_user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='history.LineageTree', verbose_name='世系姓名')),
            ],
            options={
                'verbose_name': '坟茔信息',
                'verbose_name_plural': '坟茔信息',
            },
            bases=('history.gravesbasemodel',),
        ),
        migrations.CreateModel(
            name='GravesSupplementMap',
            fields=[
                ('gravesbasemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='history.GravesBaseModel')),
                ('belong_to_user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='history.HusbandToWife', verbose_name='世系姓名')),
            ],
            options={
                'verbose_name': '坟茔补充',
                'verbose_name_plural': '坟茔补充',
            },
            bases=('history.gravesbasemodel',),
        ),
        migrations.DeleteModel(
            name='GravesMap',
        ),
    ]
