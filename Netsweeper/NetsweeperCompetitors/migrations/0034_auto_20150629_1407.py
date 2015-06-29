# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0033_auto_20150624_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('resource_file', models.FileField(upload_to='', verbose_name='Document Upload')),
                ('notes', models.TextField(blank=True, max_length=3000, verbose_name='Notes about this file')),
            ],
        ),
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('resource_category', models.CharField(max_length=255, verbose_name='Resource Category')),
                ('notes', models.TextField(blank=True, max_length=3000, verbose_name='Additional Resource Category Notes')),
            ],
        ),
        migrations.AddField(
            model_name='resourcefiles',
            name='resource',
            field=models.ForeignKey(to='NetsweeperCompetitors.Resources'),
        ),
    ]
