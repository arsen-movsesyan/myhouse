# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_houseuser_mainaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicAddress',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('str_line_1', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('str_line_2', models.CharField(max_length=255)),
                ('appt_unit', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'mh_1_account_basic_address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainHouse',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'mh_1_account_main_house',
                'managed': False,
            },
        ),
        migrations.AlterModelTable(
            name='houseuser',
            table='mh_1_account_house_user',
        ),
    ]
