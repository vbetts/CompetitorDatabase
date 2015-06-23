# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0021_auto_20150602_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='merged_with',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
