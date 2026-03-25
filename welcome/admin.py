from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('visible', 'date', 'summary',  'link')

admin.site.register(Event, EventAdmin)
