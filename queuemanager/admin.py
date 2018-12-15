from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import User

admin.site.register(Job)
admin.site.register(FeaturedPrint)
admin.site.register(RecentPrint)
#admin.site.register(Profile)



class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile
        fields=('user__id', 'user__password','user__username','user__first_name','user__last_name','user__email', 'quota', 'grade')
        
class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource


admin.site.register(Profile, ProfileAdmin)
