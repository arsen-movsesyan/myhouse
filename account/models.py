from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class BasicAddress(models.Model):
    id = models.AutoField(primary_key=True)
    str_line_1 = models.CharField(max_length=255,blank=False)
    city = models.CharField(max_length=255,blank=False)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    country = models.CharField(max_length=255,blank=False)
    str_line_2 = models.CharField(max_length=255,blank=True)
    appt_unit = models.CharField(max_length=255,blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_account_basic_address".format(settings.PROJECT_VERSION)


    def __str__(self):
	return "{0}, {1} {2}, {3}".format(
	    self.str_line_1,
	    self.city,
	    self.state,
	    self.zip_code)

class Household(models.Model):
    id = models.AutoField(primary_key=True)
    ba_id = models.ForeignKey(BasicAddress,related_name='main_household',db_column='ba_id')
    create_date = models.DateField(auto_now_add=True)
    unique_code = None

    class Meta:
	managed = False
	db_table = "mh_{0}_account_household".format(settings.PROJECT_VERSION)

#    def generate_unique_code(self):
#	if not self.unique_code:
	    


class HouseUser(models.Model):
    HUMAN_SEX = [
		('MALE',"Male"),
		('FEMALE',"Female"),
		('PREFER_NOT_TO_SAY',"Prefer not to say")]

    user_id = models.OneToOneField(settings.AUTH_USER_MODEL,
	    db_column='user_id',
	    related_name='house_user',
	    primary_key=True)

    dob = models.DateField()
    ssn_13 = models.CharField(max_length=3,blank=False)
    ssn_45 = models.CharField(max_length=2,blank=False)
    ssn_69 = models.CharField(max_length=4,blank=False)
    mh_superuser = models.BooleanField(default=False) #In addition to "is_superuser" this is for household admin
    sex =  models.CharField(max_length=255,choices=HUMAN_SEX,blank=False)
    complete_ssn = None

    class Meta:
	managed = False
	db_table = "mh_{0}_account_house_user".format(settings.PROJECT_VERSION)


    def get_complete_ssn(self,clear=False):
	if not self.complete_ssn:
	    self.complete_ssn="{0}-{1}-{2}".format(self.ssn_13,self.ssn_45,self.ssn_69)
	if clear:
	    return self.complete_ssn.replace('-','')
	return self.complete_ssn


class MapUserHousehold(models.Model):
    user_id = models.OneToOneField('HouseUser',
	    db_column='user_id',
	    primary_key=True,
	    related_name='map_to_household')
    household = models.ForeignKey('Household',
	    related_name='map_to_household')
    assign_time = models.DateTimeField(auto_now_add=True)
    self_created = models.BooleanField()

    class Meta:
	managed = False
	db_table = "mh_{0}_account_map_user_household".format(settings.PROJECT_VERSION)

