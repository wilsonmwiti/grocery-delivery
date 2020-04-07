# Register your models here.
from django.contrib import admin

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
from sellers.models import Stores, StoreLine, OpeningHours


# the module name is app_name.models


class StoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'line', 'town', 'verified', 'time_added', 'phone_number', 'email',)
    search_fields = ('town', 'name')


class LinesAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'logo', 'time_added', 'image_tag')
    search_fields = ('name',)
    # fields = []
    readonly_fields = ['image_tag', ]


class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'weekday', 'from_hour', 'to_hour', 'time_modified', 'time_added',)
    search_fields = ('id', 'store')
    readonly_fields = ['id', 'time_modified', 'time_added']


admin.site.register(OpeningHours, OpeningHoursAdmin)
admin.site.register(Stores, StoresAdmin)
admin.site.register(StoreLine, LinesAdmin)
