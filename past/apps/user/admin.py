from django.contrib import admin
# import_export
from import_export.fields import Field
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# models
from django.contrib.auth.models import User
from ..pastebins.models import Pastebin

# Register your models here.

class UserResource(resources.ModelResource):
    paste_count = Field()

    class Meta:
        model = User

    def dehydrate_paste_count(self, user):
        pastebins = Pastebin.objects.filter(user=user).count()
        return '{}'.format(pastebins)


class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource


admin.site.unregister(User)
admin.site.register(User, UserAdmin)