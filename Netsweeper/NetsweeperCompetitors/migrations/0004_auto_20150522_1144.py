# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0003_auto_20150522_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='installation',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='platform',
            name='product',
            field=models.ForeignKey(to='NetsweeperCompetitors.Product'),
        ),
    ]
