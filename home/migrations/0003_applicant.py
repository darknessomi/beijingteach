# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20151227_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(max_length=128, blank=True)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=16)),
                ('experiences', models.TextField()),
                ('added_file_url', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
