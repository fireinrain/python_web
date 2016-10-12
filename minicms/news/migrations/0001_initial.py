# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aticle',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='网址')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('published', models.BooleanField(default=True, verbose_name='正式发布')),
                ('author', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, verbose_name='作者', blank=True)),
            ],
            options={
                'verbose_name_plural': '教程',
                'verbose_name': '教程',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='栏目名称')),
                ('slug', models.CharField(db_index=True, max_length=256, verbose_name='栏目网址')),
                ('intro', models.TextField(default='', verbose_name='栏目简介')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': '栏目',
                'verbose_name': '栏目',
            },
        ),
        migrations.AddField(
            model_name='aticle',
            name='column',
            field=models.ManyToManyField(to='news.Column', verbose_name='归属栏目'),
        ),
    ]
