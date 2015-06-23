# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0022_competitor_merged_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='channel_partners',
            field=models.TextField(max_length=3000, blank=True, verbose_name='Channel Partners'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='oem_partners',
            field=models.TextField(max_length=3000, blank=True, verbose_name='OEM Partners'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='technology_partners',
            field=models.TextField(max_length=3000, blank=True, verbose_name='Technology Partners'),
        ),
    ]
