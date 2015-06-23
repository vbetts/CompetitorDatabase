# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0007_auto_20150522_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channelamount',
            name='channel',
        ),
        migrations.RemoveField(
            model_name='channelamount',
            name='company',
        ),
        migrations.RemoveField(
            model_name='technologiesamount',
            name='company',
        ),
        migrations.RemoveField(
            model_name='technologiesamount',
            name='technology',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='channels',
        ),
        migrations.RemoveField(
            model_name='competitor',
            name='technologies',
        ),
        migrations.AddField(
            model_name='competitor',
            name='appliance',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='competitor',
            name='direct',
            field=models.IntegerField(blank=True, default=0, verbose_name='Direct'),
        ),
        migrations.AddField(
            model_name='competitor',
            name='partners',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='competitor',
            name='saas',
            field=models.IntegerField(blank=True, default=0, verbose_name='SaaS'),
        ),
        migrations.DeleteModel(
            name='ChannelAmount',
        ),
        migrations.DeleteModel(
            name='Channels',
        ),
        migrations.DeleteModel(
            name='Technologies',
        ),
        migrations.DeleteModel(
            name='TechnologiesAmount',
        ),
    ]
