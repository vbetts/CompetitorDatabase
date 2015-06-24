# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0031_auto_20150624_1242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='targetmarket',
            options={'verbose_name_plural': 'Target Market', 'verbose_name': 'Target Market'},
        ),
    ]
