# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NetsweeperCompetitors', '0036_auto_20150629_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceFile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('resource_file', models.FileField(upload_to='', verbose_name='Document Upload')),
                ('notes', models.TextField(max_length=3000, blank=True, verbose_name='Notes about this file')),
            ],
            options={
                'verbose_name': 'Resource File',
                'verbose_name_plural': 'Resource Files',
            },
        ),
        migrations.RenameModel(
            old_name='Resources',
            new_name='Resource',
        ),
        migrations.RemoveField(
            model_name='resourcefiles',
            name='resource_category',
        ),
        migrations.DeleteModel(
            name='ResourceFiles',
        ),
        migrations.AddField(
            model_name='resourcefile',
            name='resource_category',
            field=models.ForeignKey(to='NetsweeperCompetitors.Resource'),
        ),
    ]
