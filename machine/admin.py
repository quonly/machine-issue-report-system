from django.contrib import admin
from .models import Machine, Report, History


class MachineAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')


class ReportAdmin(admin.ModelAdmin):
  list_display = ('id', 'machine_id', 'issue',
                  'timestamp', 'status')


class HistoryAdmin(admin.ModelAdmin):
  list_display = ('report_id', 'status', 'timestamp')


admin.site.register(Machine, MachineAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(History, HistoryAdmin)
