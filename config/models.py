from django.db import models
from django.conf import settings

# Create your models here.

class AccountType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=255)
    brief = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
	managed = False
	db_table = "mh_{0}_config_accttype".format(settings.PROJECT_VERSION)
