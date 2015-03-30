# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Enter the Title of your blog ', max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.CharField(verbose_name='Enter the body of your blog', max_length=5000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.CharField(verbose_name='Enter your comment', max_length=1000)),
                ('votes', models.IntegerField(default=0)),
                ('blog', models.ForeignKey(to='myapp.Blog')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
