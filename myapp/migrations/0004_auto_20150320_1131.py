# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_comments_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='photo',
            field=models.ImageField(upload_to='comment', default='/home/shubham/myblog/home/media/comment/image1.jpg'),
            preserve_default=True,
        ),
    ]
