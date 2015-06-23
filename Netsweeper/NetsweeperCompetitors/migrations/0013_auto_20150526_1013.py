# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0012_additionalinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='company',
            new_name='competitor',
        ),
    ]
