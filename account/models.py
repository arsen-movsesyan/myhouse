from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class BasicAddress(models.Model):
    id = models.AutoField(primary_key=True)
    str_line_1 = models.CharField(max_length=255,blank=False)
    city = models.CharField(max_length=255,blank=False)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255,blank=False)
    str_line_2 = models.CharField(max_length=255)
    appt_unit = models.CharField(max_length=255)

    class Meta:
	managed = False
	db_table = "mh_{0}_account_basic_address".format(settings.PROJECT_VERSION)


class MainHouse(models.Model):
    id = models.AutoField(primary_key=True)
    ba_id = models.ForeignKey(BasicAddress,related_name='main_household',db_column='ba_id')
    create_date = models.DateField(auto_now_add=True)
    description = models.TextField()

    class Meta:
	managed = False
	db_table = "mh_{0}_account_main_house".format(settings.PROJECT_VERSION)


class HouseUser(models.Model):
    HUMAN_SEX = [
		('MALE',"Male"),
		('FEMALE',"Female"),
		('PREFER_NOT_TO_SAY',"Prefer not to say")]

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
	    db_column='user_id',
	    related_name='house_user',
	    primary_key=True)

    dob = models.DateField()
    ssn_13 = models.CharField(max_length=3,blank=False)
    ssn_45 = models.CharField(max_length=2,blank=False)
    ssn_69 = models.CharField(max_length=4,blank=False)
    mh_superuser = models.BooleanField(default=False) #In addition to "is_superuser" this is for household admin
    sex =  models.CharField(max_length=255,choices=HUMAN_SEX,blank=False)

    class Meta:
	managed = False
	db_table = "mh_{0}_account_house_user".format(settings.PROJECT_VERSION)
