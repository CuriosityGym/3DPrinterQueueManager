from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.models import User

admin.site.register(Job)
admin.site.register(FeaturedPrint)
admin.site.register(RecentPrint)
admin.site.register(Profile)



class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields=('id', 'password','username','first_name','last_name','email', 'profile__quota', 'profile__grade')
        
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
