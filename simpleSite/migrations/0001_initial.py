# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('callName', models.CharField(unique=True, max_length=40, verbose_name='\u6240\u5c5e\u5355\u4f4d')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('realName', models.CharField(max_length=10, verbose_name='\u771f\u5b9e\u59d3\u540d')),
                ('loginName', models.CharField(unique=True, max_length=20, verbose_name='\u95e8\u6237\u5e10\u6237')),
                ('projectAccount', models.BooleanField(max_length=1, verbose_name='\u9879\u76ee\u7528\u6237,\u5141\u8bb8\u591a\u4eba\u4f7f\u7528\u540c\u4e00\u5e10\u6237\u767b\u9646')),
                ('email', models.EmailField(max_length=40, verbose_name='\u90ae\u4ef6\u5730\u5740')),
                ('phone', models.CharField(max_length=13, verbose_name='\u79fb\u52a8\u7535\u8bdd')),
                ('position', models.CharField(default='\u6559\u5de5', max_length=1, choices=[(b'T', '\u6559\u5de5'), (b'S', '\u5b66\u751f')])),
                ('story', models.TextField(max_length=50, verbose_name='\u9879\u76ee\u63cf\u8ff0')),
                ('organization', models.ForeignKey(to='simpleSite.Organization')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
