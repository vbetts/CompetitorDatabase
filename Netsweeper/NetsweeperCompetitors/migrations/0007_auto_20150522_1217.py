# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0006_auto_20150522_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChannelAmount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('percentage', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Channels',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TechnologiesAmount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('percentage', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='ChannelDirect',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='ChannelPartners',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='appliance',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='saas',
        ),
        migrations.AddField(
            model_name='technologiesamount',
            name='company',
            field=models.ForeignKey(to='NetsweeperCompetitors.Competitor'),
        ),
        migrations.AddField(
            model_name='technologiesamount',
            name='technology',
            field=models.ForeignKey(to='NetsweeperCompetitors.Technologies'),
        ),
        migrations.AddField(
            model_name='channelamount',
            name='channel',
            field=models.ForeignKey(to='NetsweeperCompetitors.Channels'),
        ),
        migrations.AddField(
            model_name='channelamount',
            name='company',
            field=models.ForeignKey(to='NetsweeperCompetitors.Competitor'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='channels',
            field=models.ManyToManyField(through='NetsweeperCompetitors.ChannelAmount', to='NetsweeperCompetitors.Channels'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='technologies',
            field=models.ManyToManyField(through='NetsweeperCompetitors.TechnologiesAmount', to='NetsweeperCompetitors.Technologies'),
        ),
    ]
