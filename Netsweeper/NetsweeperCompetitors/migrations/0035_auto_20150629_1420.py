# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0034_auto_20150629_1407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resourcefiles',
            old_name='resource',
            new_name='resource_category',
        ),
    ]
