from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
# Create your models here.

class HouseUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,related_name='house_user')
    main_account = models.ForeignKey('MainAccount',related_name='acct_users')
    dob = models.DateField()

    class Meta:
	managed = False
	db_table = "mh_{0}_acct_house_user".format(settings.PROJECT_VERSION)


class MainAccount(models.Model):
    id = models.AutoField(primary_key=True)
    create_date = models.DateField(auto_now_add=True)
    description = models.TextField()

    class Meta:
	managed = False
	db_table = "mh_{0}_acct_main_account".format(settings.PROJECT_VERSION)
