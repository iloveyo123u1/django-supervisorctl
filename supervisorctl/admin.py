from django.contrib import admin
from supervisorctl.models import Group, Host, Service 

class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', )

class HostAdmin(admin.ModelAdmin):
    pass

class ServiceAdmin(admin.ModelAdmin):
     list_display = ('name', 'path', 'host', 'group')

admin.site.register(Group, GroupAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Service, ServiceAdmin)
