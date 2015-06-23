# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0025_auto_20150618_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='number_of_categories',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
