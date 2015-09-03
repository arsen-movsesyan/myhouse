# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20150901_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mh_1_myhouse_household',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MapUserHousehold',
            fields=[
                ('user', models.OneToOneField(related_name='user_map', primary_key=True, db_column=b'user_id', serialize=False, to='people.HouseUser')),
                ('hh_superuser', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'mh_1_map_user_household',
                'managed': False,
            },
        ),
    ]
