# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0008_auto_20150522_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('review', models.TextField(blank=True, max_length=255)),
                ('company', models.ForeignKey(to='NetsweeperCompetitors.Competitor')),
            ],
        ),
        migrations.RemoveField(
            model_name='marketfeedback',
            name='company',
        ),
        migrations.DeleteModel(
            name='MarketFeedback',
        ),
    ]
