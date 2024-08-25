from django.contrib import admin
from .models import StaticMessages, Trigger, UserStatus, State


@admin.register(StaticMessages)
class SMAdmin(admin.ModelAdmin):
    list_display = ('caption', 'text')
    # readonly_fields = ('caption')

@admin.register(Trigger)
class TriggersAdmin(admin.ModelAdmin):
    list_display = ('caption', 'type')

@admin.register(UserStatus)
class USAdmin(admin.ModelAdmin):
    list_display = ('caption',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('caption',)
