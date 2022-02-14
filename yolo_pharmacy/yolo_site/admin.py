from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Company)
admin.site.register(models.Medicine)
admin.site.register(models.Employee)
admin.site.register(models.BillDetails)