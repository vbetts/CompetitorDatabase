# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0017_auto_20150602_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competitorcategories',
            old_name='details',
            new_name='subcategories',
        ),
    ]
