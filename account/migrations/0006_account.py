# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_mapuserhousehold'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('acct_name', models.CharField(max_length=255)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
                ('login_url', models.URLField()),
            ],
            options={
                'db_table': 'mh_1_account_account',
                'managed': False,
            },
        ),
    ]
