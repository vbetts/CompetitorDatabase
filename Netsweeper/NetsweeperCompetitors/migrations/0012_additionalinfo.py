# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0011_auto_20150522_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('document', models.FileField(verbose_name='Add extra documentation', upload_to='')),
                ('company', models.ForeignKey(to='NetsweeperCompetitors.Competitor')),
            ],
        ),
    ]
