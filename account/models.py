from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from people.models import HouseUser
from config.models import AccountType,AccountAttribute


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    acct_name = models.CharField(max_length=255)
    create_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(HouseUser,db_column='created_by')
    login_url = models.URLField()
    acct_type = models.ForeignKey(AccountType)
    disabled = models.BooleanField(default=False)
    disabled_date = models.DateField(blank=True)
    time_watch = models.BooleanField(default=False)
    access_login = models.CharField(max_length=255,blank=True)
    access_password = models.CharField(max_length=255,blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_account_account".format(settings.PROJECT_VERSION)



class AccountUserPermission(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account)
    user = models.ForeignKey(HouseUser)
    can_view = models.BooleanField()
    can_manage = models.BooleanField()
    can_edit = models.BooleanField()

    class Meta:
	managed = False
	db_table = "mh_{0}_account_user_permission".format(settings.PROJECT_VERSION)


class AccountAttributeValue(models.Model):
    account = models.OneToOneField(Account,
	db_column='account_id',
	primary_key=True,
	related_name='attributes')
    attribute = models.ForeignKey(AccountAttribute,
	db_column='attribute_id')
    value = models.CharField(max_length=255,blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_account_attribute_value".format(settings.PROJECT_VERSION)



class AccountTimeWatch(models.Model):
    account = models.OneToOneField(Account,
	primary_key=True,
	db_column='account_id',
	related_name='t_watch')
    auto_payment = models.BooleanField()
    month_frequency = models.IntegerField(blank=True)
    month_due_date = models.DateField(blank=True)
    initial_payment_date = models.DateField(blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_account_time_watch".format(settings.PROJECT_VERSION)


class AccountPaymentHistory(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.ForeignKey(AccountTimeWatch,
	db_column='account_id',
	related_name='payment_history')
    payment_date = models.DateField()
    payment_amount = models.CharField(max_length=30)
    confirmation_code = models.CharField(max_length=255,blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_account_payment_history".format(settings.PROJECT_VERSION)

