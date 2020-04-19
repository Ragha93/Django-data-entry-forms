from django.contrib import admin
from walkapp.models import Userprofileinfo,Mytimein,Wts_table
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User


class MytimeinAdmin(admin.ModelAdmin):
    list_filter = ['user','date']
    list_display = ['user','date']
    # list_editable = ['date']

admin.site.register(Userprofileinfo)
admin.site.register(Mytimein,MytimeinAdmin)



@admin.register(Wts_table)
class Wts_tableAdmin(ImportExportModelAdmin,admin.ModelAdmin):
        search_fields = ['asin']
        list_filter = ['allocationdate','allocatedto']
        class Meta:
            pass





# Register your models here.
