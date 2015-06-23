# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0020_competitor_acquired'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='acquired_by',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='status',
            field=models.TextField(blank=True, verbose_name='Company Status', max_length=1000),
        ),
    ]
