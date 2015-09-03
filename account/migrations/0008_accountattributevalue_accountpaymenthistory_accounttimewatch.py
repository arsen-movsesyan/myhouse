# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_accountuserpermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountAttributeValue',
            fields=[
                ('account', models.OneToOneField(related_name='attributes', primary_key=True, db_column=b'account_id', serialize=False, to='account.Account')),
                ('value', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'mh_1_account_attribute_value',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountPaymentHistory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('payment_date', models.DateField()),
                ('payment_amount', models.CharField(max_length=30)),
                ('confirmation_code', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'mh_1_account_payment_history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountTimeWatch',
            fields=[
                ('account', models.OneToOneField(related_name='t_watch', primary_key=True, db_column=b'account_id', serialize=False, to='account.Account')),
                ('auto_payment', models.BooleanField()),
                ('month_frequency', models.IntegerField(blank=True)),
                ('month_due_date', models.DateField(blank=True)),
                ('initial_payment_date', models.DateField(blank=True)),
            ],
            options={
                'db_table': 'mh_1_account_time_watch',
                'managed': False,
            },
        ),
    ]
