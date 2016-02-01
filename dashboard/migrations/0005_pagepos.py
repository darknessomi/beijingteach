# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_sitesetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagePos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('page', models.OneToOneField(related_name='position', null=True, blank=True, to='dashboard.Page')),
            ],
            options={
                'verbose_name_plural': 'Page Positons',
            },
        ),
    ]
