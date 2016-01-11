# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_applicant'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 9, 16, 10, 29, 511329, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applicant',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 9, 16, 10, 54, 13191, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
