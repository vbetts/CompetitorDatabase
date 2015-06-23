# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0010_auto_20150522_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitor',
            name='notes',
            field=models.TextField(blank=True, max_length=3000, verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='product',
            name='installation',
            field=models.ManyToManyField(blank=True, to='NetsweeperCompetitors.Installation'),
        ),
        migrations.AlterField(
            model_name='product',
            name='platform',
            field=models.ManyToManyField(blank=True, to='NetsweeperCompetitors.Platform'),
        ),
    ]
