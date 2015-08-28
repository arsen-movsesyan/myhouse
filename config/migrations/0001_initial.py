# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('type_name', models.CharField(max_length=255)),
                ('brief', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'mh_1_config_accttype',
                'managed': False,
            },
        ),
    ]
