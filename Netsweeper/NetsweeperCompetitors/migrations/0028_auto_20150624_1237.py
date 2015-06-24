# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0027_auto_20150624_1208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='additionalinfo',
            options={'verbose_name_plural': 'Additional Info'},
        ),
    ]
