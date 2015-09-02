# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountUserPermission',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('can_view', models.BooleanField()),
                ('can_manage', models.BooleanField()),
                ('can_edit', models.BooleanField()),
            ],
            options={
                'db_table': 'mh_1_account_user_permission',
                'managed': False,
            },
        ),
    ]
