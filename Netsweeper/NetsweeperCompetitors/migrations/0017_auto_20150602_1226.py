# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0016_auto_20150526_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CompetitorCategories',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('details', models.TextField(max_length=3000, null=True, verbose_name='Category Details', blank=True)),
                ('category', models.ForeignKey(to='NetsweeperCompetitors.Category')),
                ('competitor', models.ForeignKey(to='NetsweeperCompetitors.Competitor')),
            ],
        ),
        migrations.AddField(
            model_name='competitor',
            name='categories',
            field=models.ManyToManyField(to='NetsweeperCompetitors.Category', through='NetsweeperCompetitors.CompetitorCategories'),
        ),
    ]
