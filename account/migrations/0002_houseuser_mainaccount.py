# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dob', models.DateField()),
            ],
            options={
                'db_table': 'mh_1_acct_house_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainAccount',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'mh_1_acct_main_account',
                'managed': False,
            },
        ),
    ]
