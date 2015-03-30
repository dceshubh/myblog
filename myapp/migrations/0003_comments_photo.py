# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20150316_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='photo',
            field=models.ImageField(upload_to='comment', default=datetime.datetime(2015, 3, 20, 5, 42, 35, 108456, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
