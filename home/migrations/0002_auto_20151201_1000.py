# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('is_valid', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('snippet_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='dashboard.Snippet')),
                ('applicant', models.ForeignKey(related_name='messages', to='home.Applicant')),
            ],
            bases=('dashboard.snippet',),
        ),
        migrations.AlterField(
            model_name='imgpos',
            name='img',
            field=models.ForeignKey(related_name='positions', to='dashboard.Img'),
        ),
        migrations.AlterField(
            model_name='snippetpos',
            name='snippet',
            field=models.ForeignKey(related_name='positions', to='dashboard.Snippet'),
        ),
    ]
