# Generated by Django 2.2.5 on 2020-05-11 15:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')], default='pxjg', max_length=20, verbose_name='机构类别'),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(upload_to='org/%Y%m', verbose_name='logo'),
        ),
    ]