# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0037_auto_20150629_1424'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Resource',
            new_name='ResourceCategory',
        ),
        migrations.AlterModelOptions(
            name='resourcecategory',
            options={'verbose_name_plural': 'Resource Categories', 'verbose_name': 'Resource Category'},
        ),
    ]
