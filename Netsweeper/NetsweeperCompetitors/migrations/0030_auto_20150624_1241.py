# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0029_auto_20150624_1239'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyfeatures',
            options={'verbose_name_plural': 'Product Features'},
        ),
        migrations.AlterModelOptions(
            name='competitorcategories',
            options={'verbose_name_plural': 'Competitor Filtering Categories'},
        ),
        migrations.AlterModelOptions(
            name='targetmarket',
            options={'verbose_name': 'Target Market'},
        ),
        migrations.AlterField(
            model_name='competitor',
            name='target_Market',
            field=models.ManyToManyField(to='NetsweeperCompetitors.TargetMarket', verbose_name='Target Markets'),
        ),
    ]
