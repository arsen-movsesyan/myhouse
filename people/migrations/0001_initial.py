# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseUser',
            fields=[
                ('auth_user', models.OneToOneField(related_name='house_user', primary_key=True, db_column=b'user_id', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.IntegerField()),
                ('dob', models.DateField()),
                ('ssn_13', models.CharField(max_length=3)),
                ('ssn_45', models.CharField(max_length=2)),
                ('ssn_69', models.CharField(max_length=4)),
                ('mh_superuser', models.BooleanField(default=False)),
                ('sex', models.CharField(max_length=255, choices=[(b'MALE', b'Male'), (b'FEMALE', b'Female')])),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('title', models.CharField(blank=True, max_length=255, choices=[(b'MR', b'Mr.'), (b'MRS', b'Mrs.'), (b'MS', b'Ms.')])),
                ('suffix', models.CharField(blank=True, max_length=255, choices=[(b'SR', b'Senior'), (b'JR', b'Junior')])),
                ('disabled', models.BooleanField(default=False)),
                ('disabled_at', models.DateField()),
            ],
            options={
                'db_table': 'mh_1_account_house_user',
                'managed': False,
            },
        ),
    ]
