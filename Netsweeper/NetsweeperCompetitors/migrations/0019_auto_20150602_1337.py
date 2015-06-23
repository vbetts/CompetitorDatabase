# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0018_auto_20150602_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitorcategories',
            name='subcategories',
        ),
        migrations.AddField(
            model_name='competitorcategories',
            name='details',
            field=models.TextField(max_length=3000, null=True, verbose_name='Sub-Categories', blank=True),
        ),
    ]
