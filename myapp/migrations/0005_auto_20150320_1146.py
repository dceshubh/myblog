# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20150320_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='photo',
            field=models.ImageField(upload_to='comment', default='/static/images/image1.jpg'),
            preserve_default=True,
        ),
    ]
