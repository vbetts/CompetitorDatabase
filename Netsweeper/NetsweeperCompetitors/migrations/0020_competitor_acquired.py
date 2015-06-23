# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0019_auto_20150602_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitor',
            name='acquired',
            field=models.BooleanField(default=False, verbose_name='Acquired'),
            preserve_default=False,
        ),
    ]
