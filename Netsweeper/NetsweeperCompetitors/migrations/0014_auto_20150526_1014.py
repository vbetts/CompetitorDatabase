# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0013_auto_20150526_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='additionalinfo',
            old_name='company',
            new_name='competitor',
        ),
        migrations.RenameField(
            model_name='companyfeatures',
            old_name='company',
            new_name='competitor',
        ),
        migrations.RenameField(
            model_name='globalmarketshare',
            old_name='company',
            new_name='competitor',
        ),
        migrations.RenameField(
            model_name='revenueestimate',
            old_name='companies',
            new_name='competitor',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='company',
            new_name='competitor',
        ),
        migrations.RenameField(
            model_name='verticalmarketshare',
            old_name='company',
            new_name='competitor',
        ),
    ]
