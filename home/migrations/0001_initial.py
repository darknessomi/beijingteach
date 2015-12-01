# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImgPos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('img', models.ForeignKey(related_name='position', to='dashboard.Img')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SnippetPos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('snippet', models.ForeignKey(related_name='position', to='dashboard.Snippet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
