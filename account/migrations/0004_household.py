# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20150820_1138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'mh_1_account_household',
                'managed': False,
            },
        ),
    ]
