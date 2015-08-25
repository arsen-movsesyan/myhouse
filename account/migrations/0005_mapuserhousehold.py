# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_household'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapUserHousehold',
            fields=[
                ('user_id', models.OneToOneField(related_name='map_to_household', primary_key=True, db_column=b'user_id', serialize=False, to='account.HouseUser')),
                ('household', models.OneToOneField(primary_key=True, to='account.Household')),
                ('assigned_time', models.DateTimeField(auto_now_add=True)),
                ('self_created', models.BooleanField()),
            ],
            options={
                'db_table': 'mh_1_account_map_user_household',
                'managed': False,
            },
        ),
    ]
