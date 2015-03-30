# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='votes',
        ),
        migrations.AddField(
            model_name='comments',
            name='username',
            field=models.CharField(default='anonymous', verbose_name='Enter your name', max_length=50),
            preserve_default=True,
        ),
    ]
