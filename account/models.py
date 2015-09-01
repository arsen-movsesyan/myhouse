from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from people.models import HouseUser
from config.models import AccountType

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
