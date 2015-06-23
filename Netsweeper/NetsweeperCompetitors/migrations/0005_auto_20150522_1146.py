# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0004_auto_20150522_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='platform',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='platform',
            field=models.ManyToManyField(to='NetsweeperCompetitors.Platform'),
        ),
    ]
