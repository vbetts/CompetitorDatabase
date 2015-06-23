# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0024_auto_20150612_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='appliance',
            field=models.DecimalField(help_text='Enter in format: 00.00', default=0, decimal_places=2, blank=True, max_digits=12),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='saas',
            field=models.DecimalField(verbose_name='SaaS', max_digits=12, decimal_places=2, help_text='Enter in format: 00.00', default=0, blank=True),
        ),
    ]
