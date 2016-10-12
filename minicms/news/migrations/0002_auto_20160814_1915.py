# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aticle',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 14, 11, 15, 21, 775807, tzinfo=utc), auto_now_add=True, verbose_name='发表时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aticle',
            name='update_time',
            field=models.DateTimeField(null=True, auto_now=True, verbose_name='更新时间'),
        ),
    ]
