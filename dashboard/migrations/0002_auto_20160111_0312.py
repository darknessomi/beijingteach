# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='imgpos',
            name='img',
            field=models.ForeignKey(related_name='position', blank=True, to='dashboard.Img', null=True),
        ),
    ]
