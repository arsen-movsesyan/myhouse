from django.db import models
from django.conf import settings
from django.db.models import Max
from django.utils import timezone

from datetime import date,timedelta
from config.models import VehicleType
from people.models import HouseUser


# Create your models here.

class VehicleGeneric(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_type = models.ForeignKey(VehicleType,db_column='type_id')
    date_registered = models.DateField()
    date_purchased = models.DateField()

    class Meta:
	managed = False
	db_table = "mh_{0}_vehicle_generic".format(settings.PROJECT_VERSION)

class VehicleCar(models.Model):
    vehicle = models.OneToOneField(VehicleGeneric,primary_key=True,db_column='id',related_name='car')
    year_produced = models.CharField(max_length=4)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    milage_purchased = models.IntegerField(blank=True)
    milage_registered = models.IntegerField(blank=True)
    owned_by = models.ForeignKey(HouseUser,db_column='owned_by')
    vin = models.CharField(max_length=255)
    non_operational = models.BooleanField()
    license_plate = models.CharField(max_length=255,blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_vehicle_car".format(settings.PROJECT_VERSION)

    def get_renewal_due_date(self):
	ret = dict()
	latest = self.vehicle.renewal.aggregate(Max('renewal_date'))['renewal_date__max']
	if not latest:
	    ret['due_date'] = None
	    ret['days_left'] = None
	else:
	    latest += timedelta(days=365)
	    days_left = (latest - date.today()).days
	    ret['due_date'] = latest
	    ret['days_left'] = days_left
	return ret

class VehicleCarUserPermission(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(HouseUser,db_column='user_id',related_name='permission_cars')
    car = models.ForeignKey(VehicleCar,db_column='car_id')
    can_operate = models.BooleanField()

    class Meta:
	managed = False
	db_table = "mh_{0}_vehicle_car_user_permission".format(settings.PROJECT_VERSION)


class VehicleRenewal(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle = models.ForeignKey(VehicleGeneric,db_column='vehicle_id',related_name='renewal')
    renewal_date = models.DateField(default=timezone.now)
    renewal_amount = models.CharField(max_length=255,blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_vehicle_renewal".format(settings.PROJECT_VERSION)
	ordering = ['renewal_date']


