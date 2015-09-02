# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountAttribute',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('attribute_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'mh_1_config_acctattribute',
                'managed': False,
            },
        ),
    ]
