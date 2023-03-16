from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import paydata,items,invntor

# Register your models here.
@admin.register(paydata)
class paydataAdmin(ImportExportModelAdmin):
    pass
@admin.register(items)
class itemsAdmin(ImportExportModelAdmin):
    pass
@admin.register(invntor)
class invntorAdmin(ImportExportModelAdmin):
    pass