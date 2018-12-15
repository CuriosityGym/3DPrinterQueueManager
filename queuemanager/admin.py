from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import User

admin.site.register(Job)
admin.site.register(FeaturedPrint)
admin.site.register(RecentPrint)



#Add Upload Options for Users
class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields=('id', 'password','username','first_name','last_name','email')
        
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

admin.site.unregister(User)
admin.site.register(User, UserAdmin)



# Add Upload Options for Profiles
class ProfileResource(resources.ModelResource):
    class Meta:
        model = Profile
        #fields=('id', 'password','username','first_name','last_name','email')
        
class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource


admin.site.register(Profile, ProfileAdmin)
