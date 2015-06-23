# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketFeedback',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.TextField(blank=True, max_length=1000)),
                ('urlDB', models.CharField(blank=True, max_length=255)),
                ('price', models.DecimalField(default=0, blank=True, help_text='Enter in format: 00.00', decimal_places=2, max_digits=12)),
                ('notes', models.TextField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='TargetMarket',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='opportunities',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='prodName',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='prodStatus',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='threats',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='urlDB',
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(to='NetsweeperCompetitors.Competitor'),
        ),
        migrations.AddField(
            model_name='marketfeedback',
            name='company',
            field=models.ForeignKey(to='NetsweeperCompetitors.Competitor'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='targetMarket',
            field=models.ManyToManyField(to='NetsweeperCompetitors.TargetMarket'),
        ),
    ]
