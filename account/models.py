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
    ba = models.ForeignKey(BasicAddress,related_name='main_household',db_column='ba_id')
    create_date = models.DateField(auto_now_add=True)
    unique_code = None

    class Meta:
	managed = False
	db_table = "mh_{0}_account_household".format(settings.PROJECT_VERSION)

#    def generate_unique_code(self):
#	if not self.unique_code:
	    


class HouseUser(models.Model):
    HUMAN_SEX = [('MALE',"Male"),('FEMALE',"Female")]
    HUMAN_TITLE = [
	('MR','Mr.'),
	('MRS','Mrs.'),
	('MS','Ms.'),
    ]
    HUMAN_SUFFIX = [
	('SR','Senior'),
	('JR','Junior'),
    ]

    auth_user = models.OneToOneField(settings.AUTH_USER_MODEL,
	    db_column='user_id',
	    related_name='house_user',
	    primary_key=True)
    created_by = models.IntegerField(blank=False)
    dob = models.DateField()
    ssn_13 = models.CharField(max_length=3,blank=False)
    ssn_45 = models.CharField(max_length=2,blank=False)
    ssn_69 = models.CharField(max_length=4,blank=False)
    mh_superuser = models.BooleanField(default=False) #In addition to "is_superuser" this is for household admin
    sex =  models.CharField(max_length=255,choices=HUMAN_SEX,blank=False)
    first_name = models.CharField(max_length=255,blank=False)
    last_name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(max_length=255,blank=False)
    title = models.CharField(max_length=255,choices=HUMAN_TITLE,blank=True)
    suffix = models.CharField(max_length=255,choices=HUMAN_SUFFIX,blank=True)
    disabled = models.BooleanField(default=False)
    disabled_at = models.DateField()
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

    def __str__(self):
	return "{0} {1}".format(self.first_name,self.last_name)

class MapUserHousehold(models.Model):
    user = models.OneToOneField('HouseUser',db_column='user_id',primary_key=True
	,related_name='to_household')
    household = models.ForeignKey('Household',related_name='belong_users')

    class Meta:
	managed = False
	db_table = "mh_{0}_account_map_user_household".format(settings.PROJECT_VERSION)


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    acct_name = models.CharField(max_length=255)
    create_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('HouseUser',db_column='created_by')
    login_url = models.URLField()
    acct_type = models.ForeignKey('config.AccountType')

    class Meta:
	managed = False
	db_table = "mh_{0}_account_account".format(settings.PROJECT_VERSION)
