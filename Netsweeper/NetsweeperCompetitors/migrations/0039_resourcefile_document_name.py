# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0038_auto_20150629_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcefile',
            name='document_name',
            field=models.CharField(max_length=255, verbose_name='Document Name', default='document name'),
            preserve_default=False,
        ),
    ]
