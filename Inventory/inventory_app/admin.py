from django.contrib import admin
from .models import *


class EqmAdminInline(admin.TabularInline):
    model = Equipment
    extra = 1


class UserAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Employees._meta.fields]
    search_fields = [ search.name for search in Employees._meta.fields]
    inlines = [EqmAdminInline]

    class Meta:
        model = Employees


admin.site.register(Employees, UserAdmin)
admin.site.register(Type)


class EqmAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Equipment._meta.fields]
    # search_fields = [fields.name for fields in Equipment._meta.fields]
    search_fields = ['inventory_number','name','is_active','is_license','is_license']

    class Meta:
        model = Equipment

admin.site.register(Equipment, EqmAdmin)


