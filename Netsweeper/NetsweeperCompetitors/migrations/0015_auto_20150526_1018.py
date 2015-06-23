# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0014_auto_20150526_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompetitorFeatures',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('featureSpecs', models.TextField(blank=True, verbose_name='Technical Details', null=True, max_length=3000)),
            ],
        ),
        migrations.RemoveField(
            model_name='companyfeatures',
            name='competitor',
        ),
        migrations.RemoveField(
            model_name='companyfeatures',
            name='feature',
        ),
        migrations.AlterField(
            model_name='competitor',
            name='features',
            field=models.ManyToManyField(through='NetsweeperCompetitors.CompetitorFeatures', to='NetsweeperCompetitors.Feature'),
        ),
        migrations.DeleteModel(
            name='CompanyFeatures',
        ),
        migrations.AddField(
            model_name='competitorfeatures',
            name='competitor',
            field=models.ForeignKey(to='NetsweeperCompetitors.Competitor'),
        ),
        migrations.AddField(
            model_name='competitorfeatures',
            name='feature',
            field=models.ForeignKey(to='NetsweeperCompetitors.Feature'),
        ),
    ]
