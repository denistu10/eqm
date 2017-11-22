from django.contrib import admin
from .models import *


class EqmAdminInline(admin.TabularInline):
    model = Equipment
    extra = 1

class UserAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Users._meta.fields]
    search_fields = [ search.name for search in Users._meta.fields]
    inlines = [EqmAdminInline]

    class Meta:
        model = Users


admin.site.register(Users, UserAdmin)


class EqmAdmin(admin.ModelAdmin):
    list_display = [ field.name for field in Equipment._meta.fields]
    search_fields = [search.name for search in Users._meta.fields]


    class Meta:
        model = Equipment

admin.site.register(Equipment,EqmAdmin)
