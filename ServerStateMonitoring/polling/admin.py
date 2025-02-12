from django.contrib import admin
from .models import Server, ServerStatus, Incident

class ServerStatusInline(admin.TabularInline):
    model = ServerStatus
    extra = 0

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'endpoint')
    search_fields = ('name', 'endpoint')
    inlines = [ServerStatusInline]

@admin.register(ServerStatus)
class ServerStatusAdmin(admin.ModelAdmin):
    list_display = ('server', 'cpu', 'mem', 'disk', 'uptime', 'timestamp')
    list_filter = ('server', 'timestamp')
    search_fields = ('server__name',)
    date_hierarchy = 'timestamp'

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('server', 'parameter', 'value', 'start_time', 'end_time', 'resolved')
    list_filter = ('server', 'parameter', 'resolved')
    search_fields = ('server__name',)
    date_hierarchy = 'start_time'