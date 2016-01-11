# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='visitor',
            field=models.ForeignKey(related_name='messages', to='home.Visitor', null=True),
        ),
    ]
