# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0035_auto_20150629_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcefiles',
            options={'verbose_name_plural': 'Resource Files', 'verbose_name': 'Resource File'},
        ),
        migrations.AlterModelOptions(
            name='resources',
            options={'verbose_name_plural': 'Resources', 'verbose_name': 'Resource'},
        ),
    ]
