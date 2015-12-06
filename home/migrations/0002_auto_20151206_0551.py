# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imgpos',
            options={'verbose_name_plural': 'Img Positons'},
        ),
        migrations.AlterModelOptions(
            name='snippetpos',
            options={'verbose_name_plural': 'Snippet Positons'},
        ),
        migrations.AlterField(
            model_name='imgpos',
            name='img',
            field=models.ForeignKey(related_name='position', to='dashboard.Img'),
        ),
        migrations.AlterField(
            model_name='snippetpos',
            name='snippet',
            field=models.OneToOneField(related_name='position', null=True, blank=True, to='dashboard.Snippet'),
        ),
    ]
