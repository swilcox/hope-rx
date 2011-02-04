from django.contrib import admin

from locations.models import Location, LocationType


class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name','location_type']


class LocationTypeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location,LocationAdmin)
admin.site.register(LocationType,LocationTypeAdmin)