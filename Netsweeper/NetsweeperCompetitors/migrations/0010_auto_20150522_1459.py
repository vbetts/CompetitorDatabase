# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0009_auto_20150522_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='notes',
            field=models.TextField(verbose_name='Strengths', max_length=3000, blank=True),
        ),
        migrations.AlterField(
            model_name='companyfeatures',
            name='featureSpecs',
            field=models.TextField(verbose_name='Technical Details', max_length=3000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='focus',
            field=models.TextField(verbose_name='Company Focus', max_length=3000, blank=True),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='strengths',
            field=models.TextField(verbose_name='Strengths', max_length=3000, blank=True),
        ),
        migrations.AlterField(
            model_name='competitor',
            name='weaknesses',
            field=models.TextField(verbose_name='Weaknesses', max_length=3000, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='notes',
            field=models.TextField(max_length=3000, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.TextField(max_length=3000, blank=True),
        ),
    ]
