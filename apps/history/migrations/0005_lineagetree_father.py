# Generated by Django 2.2 on 2020-05-22 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0004_auto_20200522_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineagetree',
            name='father',
            field=models.CharField(default='', max_length=50, verbose_name='父亲名'),
        ),
    ]
