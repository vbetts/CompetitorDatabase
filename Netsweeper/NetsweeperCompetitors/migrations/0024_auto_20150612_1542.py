# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0023_auto_20150612_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='channel_partners',
            field=models.TextField(verbose_name='Channel Partners', blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='oem_partners',
            field=models.TextField(verbose_name='OEM Partners', blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='technology_partners',
            field=models.TextField(verbose_name='Technology Partners', blank=True, max_length=5000),
        ),
    ]
