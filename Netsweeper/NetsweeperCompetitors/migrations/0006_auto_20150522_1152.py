# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0005_auto_20150522_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='installation',
        ),
        migrations.AddField(
            model_name='product',
            name='installation',
            field=models.ManyToManyField(to='NetsweeperCompetitors.Installation'),
        ),
    ]
