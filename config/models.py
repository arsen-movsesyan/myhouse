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

class VehicleType(models.Model):
    id = models.AutoField(primary_key=True)
    vehicle_type = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_config_vehicle_type".format(settings.PROJECT_VERSION)

class DocumentType(models.Model):
    id = models.AutoField(primary_key=True)
    document_type = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
	managed = False
	db_table = "mh_{0}_config_document_type".format(settings.PROJECT_VERSION)


class DocumentAttribute(models.Model):
    ATTRIBUTE_FORMAT = [('DATE','Date'),('INTEGER','Integer'),('STRING','String')]

    id = models.AutoField(primary_key=True)
#    doc_type = models.ForeignKey(DocumentType,db_column='doc_type_id',related_name='doc_attributes')
    attribute = models.CharField(max_length=255)
    attribute_format = models.CharField(max_length=255,
	blank=True,
	choices=ATTRIBUTE_FORMAT,
	default='STRING')
    time_watch = models.BooleanField()

    class Meta:
	managed = False
	db_table = "mh_{0}_config_document_attribute".format(settings.PROJECT_VERSION)


class MapDocumentAttribute(models.Model):
    id = models.AutoField(primary_key=True)
    doc_type = models.ForeignKey(DocumentType,db_column='doc_type_id',related_name='doc_attributes')
    attribute = models.OneToOneField(DocumentAttribute,db_column='attr_id')
    attached = models.BooleanField()

    class Meta:
	managed = False
	db_table = "mh_{0}_config_map_doc_attribute".format(settings.PROJECT_VERSION)
    