from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import invntor,items

# Register your models here.
@admin.register(invntor)
class invntorAdmin(ImportExportModelAdmin):
    pass
@admin.register(items)
class itemsAdmin(ImportExportModelAdmin):
    pass