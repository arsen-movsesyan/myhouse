from django.contrib import admin

# Register your models here.
from config.models import *

admin.site.register(AccountType)
admin.site.register(AccountAttribute)
admin.site.register(VehicleType)
admin.site.register(DocumentType)
admin.site.register(DocumentAttribute)
admin.site.register(MapDocumentAttribute)
