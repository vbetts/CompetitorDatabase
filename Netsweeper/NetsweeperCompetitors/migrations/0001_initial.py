# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Data Source Name', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('featureSpecs', models.TextField(verbose_name='Technical Details', blank=True, null=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Company Name', max_length=255)),
                ('status', models.TextField(verbose_name='Company Status', blank=True, max_length=255)),
                ('focus', models.TextField(verbose_name='Company Focus', blank=True, max_length=1000)),
                ('ChannelDirect', models.IntegerField(default=0, verbose_name='Direct', help_text='Enter percentage numbers only', blank=True)),
                ('ChannelPartners', models.IntegerField(default=0, verbose_name='Partners', help_text='Enter percentage numbers only', blank=True)),
                ('prodName', models.CharField(verbose_name='Product Name', blank=True, max_length=255)),
                ('prodStatus', models.TextField(verbose_name='Product Status', blank=True, max_length=255)),
                ('urlDB', models.CharField(verbose_name='URL Database', blank=True, max_length=255)),
                ('url', models.URLField(verbose_name='Website', blank=True, max_length=255)),
                ('appliance', models.IntegerField(default=0, verbose_name='Appliance', help_text='Enter percentage numbers only', blank=True)),
                ('saas', models.IntegerField(default=0, verbose_name='SaaS', help_text='Enter percentage numbers only', blank=True)),
                ('strengths', models.TextField(verbose_name='Strengths', blank=True, max_length=1000)),
                ('weaknesses', models.TextField(verbose_name='Weaknesses', blank=True, max_length=1000)),
                ('opportunities', models.TextField(verbose_name='Opportunities', blank=True, max_length=1000)),
                ('threats', models.TextField(verbose_name='Threats', blank=True, max_length=1000)),
                ('last_updated', models.DateTimeField(verbose_name='Last Updated', auto_now=True)),
                ('dataSource', models.ManyToManyField(to='NetsweeperCompetitors.CompanyDataSource')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalMarketShare',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('share', models.DecimalField(default=0, decimal_places=2, help_text='Enter in format: 00.00', max_digits=12, blank=True)),
                ('company', models.ForeignKey(to='NetsweeperCompetitors.Competitor')),
                ('market', models.ForeignKey(to='NetsweeperCompetitors.GlobalMarket')),
            ],
        ),
        migrations.CreateModel(
            name='RevenueDataSource',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Data Source Name', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RevenueEstimate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('totalRevenue', models.DecimalField(verbose_name='Estimated Total Revenue (millions)', help_text='Enter in format: 00.00', max_digits=12, decimal_places=2, blank=True, default=0)),
                ('filteringRevenue', models.DecimalField(verbose_name='Estimated Filtering Revenue (millions)', help_text='Enter in format: 00.00', max_digits=12, decimal_places=2, blank=True, default=0)),
                ('companies', models.ForeignKey(to='NetsweeperCompetitors.Competitor')),
                ('dataSource', models.ForeignKey(to='NetsweeperCompetitors.RevenueDataSource')),
            ],
        ),
        migrations.CreateModel(
            name='VerticalMarket',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='VerticalMarketShare',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('share', models.DecimalField(default=0, decimal_places=2, help_text='Enter in format: 00.00', max_digits=12, blank=True)),
                ('company', models.ForeignKey(to='NetsweeperCompetitors.Competitor')),
                ('market', models.ForeignKey(to='NetsweeperCompetitors.VerticalMarket')),
            ],
        ),
        migrations.AddField(
            model_name='competitor',
            name='features',
            field=models.ManyToManyField(through='NetsweeperCompetitors.CompanyFeatures', to='NetsweeperCompetitors.Feature'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='globalMarket',
            field=models.ManyToManyField(through='NetsweeperCompetitors.GlobalMarketShare', to='NetsweeperCompetitors.GlobalMarket'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='verticalMarket',
            field=models.ManyToManyField(through='NetsweeperCompetitors.VerticalMarketShare', to='NetsweeperCompetitors.VerticalMarket'),
        ),
        migrations.AddField(
            model_name='companyfeatures',
            name='company',
            field=models.ForeignKey(to='NetsweeperCompetitors.Competitor'),
        ),
        migrations.AddField(
            model_name='companyfeatures',
            name='feature',
            field=models.ForeignKey(to='NetsweeperCompetitors.Feature'),
        ),
    ]
