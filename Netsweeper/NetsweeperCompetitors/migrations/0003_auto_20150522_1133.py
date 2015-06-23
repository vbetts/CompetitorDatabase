# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0002_auto_20150522_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competitor',
            old_name='targetMarket',
            new_name='target_Market',
        ),
        migrations.RenameField(
            model_name='globalmarketshare',
            old_name='market',
            new_name='global_market',
        ),
        migrations.RenameField(
            model_name='verticalmarketshare',
            old_name='market',
            new_name='vertical_market',
        ),
        migrations.AlterField(
            model_name='product',
            name='urlDB',
            field=models.CharField(verbose_name='URL Database', blank=True, max_length=255),
        ),
    ]
