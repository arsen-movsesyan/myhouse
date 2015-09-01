from django.db import models
from django.conf import settings

# Create your models here.

class AccountType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255)
    brief = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_config_accttype".format(settings.PROJECT_VERSION)

    def __str__(self):
	return self.type_name

class AccountAttribute(models.Model):
    id = models.AutoField(primary_key=True)
    attribute_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_config_acctattribute".format(settings.PROJECT_VERSION)

    def __str__(self):
	return self.attribute_name
