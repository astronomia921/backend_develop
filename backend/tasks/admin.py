from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'team_lead_user',
                    'employee_user', 'task_status',
                    'task_priority')
    list_filter = ('task_status', 'task_priority')
    search_fields = ('task_title',
                     'team_lead_user__first_name',
                     'employee_user__first_name')
    readonly_fields = ('task_date_start', 'task_date_modified', 'is_expired')
    fieldsets = (
        ('Task Details', {
            'fields': ('task_title', 'team_lead_user',
                       'employee_user', 'task_description')
        }),
        ('Date Information', {
            'fields': ('task_date_start',
                       'task_date_modified',
                       'task_date_finish')
        }),
        ('Status and Priority', {
            'fields': ('task_status', 'task_priority')
        }),
        ('Read-only Fields', {
            'fields': ('is_expired',),
            'classes': ('collapse',),
        }),
    )
