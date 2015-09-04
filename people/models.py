from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

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
#    mh_superuser = models.BooleanField(default=False) #In addition to "is_superuser" this is for household admin
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
	db_table = "mh_{0}_people_house_user".format(settings.PROJECT_VERSION)


    def get_complete_ssn(self,clear=False):
	if not self.complete_ssn:
	    self.complete_ssn="{0}-{1}-{2}".format(self.ssn_13,self.ssn_45,self.ssn_69)
	if clear:
	    return self.complete_ssn.replace('-','')
	return self.complete_ssn

    def __unicode__(self):
	return "{0} {1}".format(self.first_name,self.last_name)

    def is_hh_superuser(self):
	map_obj = self.user_map
	return map_obj.hh_superuser


    def get_other_users(self):
	my_household = self.user_map.household
	other_users = MapUserHousehold.objects.filter(household_id=my_household.id).exclude(pk=self)
	return other_users


class Household(models.Model):
    id = models.AutoField(primary_key=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_myhouse_household".format(settings.PROJECT_VERSION)



class MapUserHousehold(models.Model):
    user = models.OneToOneField(HouseUser,
	db_column = 'user_id',
	primary_key = True,
	related_name = 'user_map')
    household = models.ForeignKey(Household,db_column='household_id')
    hh_superuser = models.BooleanField(default=False)

    class Meta:
	managed = False
	db_table = "mh_{0}_map_user_household".format(settings.PROJECT_VERSION)
