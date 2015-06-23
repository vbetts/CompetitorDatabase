# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0015_auto_20150526_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyFeatures',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('featureSpecs', models.TextField(blank=True, null=True, max_length=3000, verbose_name='Technical Details')),
            ],
        ),
        migrations.RenameModel(
            old_name='CompanyDataSource',
            new_name='CompetitorDataSource',
        ),
        migrations.RemoveField(
            model_name='competitorfeatures',
            name='competitor',
        ),
        migrations.RemoveField(
            model_name='competitorfeatures',
            name='feature',
        ),
        migrations.AlterField(
            model_name='competitor',
            name='features',
            field=models.ManyToManyField(through='NetsweeperCompetitors.CompanyFeatures', to='NetsweeperCompetitors.Feature'),
        ),
        migrations.DeleteModel(
            name='CompetitorFeatures',
        ),
        migrations.AddField(
            model_name='companyfeatures',
            name='competitor',
            field=models.ForeignKey(to='NetsweeperCompetitors.Competitor'),
        ),
        migrations.AddField(
            model_name='companyfeatures',
            name='feature',
            field=models.ForeignKey(to='NetsweeperCompetitors.Feature'),
        ),
    ]
