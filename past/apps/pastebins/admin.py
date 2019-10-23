from django.contrib import admin
# import_export
from import_export.fields import Field
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# models
from .models import Pastebin


# Register your models here.

class PastebinResource(resources.ModelResource):
    username = Field()
    class Meta:
        model = Pastebin

    def dehydrate_username(self, pastebin):
        return '{}'.format(pastebin.user.username)


class PastebinAdmin(ImportExportModelAdmin):

    resource_class = PastebinResource


admin.site.register(Pastebin, PastebinAdmin)