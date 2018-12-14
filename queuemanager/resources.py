from import_export import resources
class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UserAdmin(ExportMixin, UserAdmin):
    resource_class = UserResource
    pass


