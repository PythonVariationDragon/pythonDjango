# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aixianfeng', '0004_shop'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=20)),
                ('pd', models.CharField(max_length=10)),
            ],
        ),
    ]
