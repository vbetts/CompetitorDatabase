# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0026_competitor_number_of_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='dataSource',
            field=models.ManyToManyField(verbose_name='Competitor Data Sources', to='NetsweeperCompetitors.CompetitorDataSource'),
        ),
    ]
