# your_app/admin_views.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import IPDatabase

class TrafficAdminView(admin.ModelAdmin):
    change_list_template = "admin/traffic.html"

    def changelist_view(self, request, extra_context=None):
        # Optionally pass additional context here
        context = {
            'ip_data': IPDatabase.objects.all(),
            'title': 'Traffic Map'
        }
        return super().changelist_view(request, extra_context=context)

# Register the custom view in the admin
admin_site = admin.AdminSite()
admin_site.register(IPDatabase, TrafficAdminView)
