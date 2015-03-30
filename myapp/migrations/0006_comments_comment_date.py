# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20150320_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_date',
            field=models.DateTimeField(verbose_name='comment date', default=datetime.datetime(2015, 3, 20, 12, 21, 14, 270224)),
            preserve_default=True,
        ),
    ]
