from django.contrib import admin
from .models import StaticMessages


@admin.register(StaticMessages)
class SMAdmin(admin.ModelAdmin):
    list_display = ('caption', 'text')
    # readonly_fields = ('caption')
