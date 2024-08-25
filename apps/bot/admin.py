from django.contrib import admin
from .models import StaticMessages, Trigger, UserStatus, State


@admin.register(StaticMessages)
class SMAdmin(admin.ModelAdmin):
    list_display = ('caption', 'text')
    # fields = [("caption", "text", "keyboard", "delay"),("state", "user_status", "trigger"),"auto_next", "new_state", "new_status"]
    # readonly_fields = ('caption')
    fieldsets = (
        (
            None,
            {
                "fields": ("caption", "text", ("keyboard", "delay")),
            },
        ),
        (
            "Входные условия",
            {
                # "classes": ["wide"],
                "fields": ("state", "user_status", "trigger"),
            },
        ),
        (
            "Побочные эффекты",
            {
                # "classes": ["collapse"],
                "fields": ("auto_next", "new_state", "new_status"),
            },
        ),
    )

@admin.register(Trigger)
class TriggersAdmin(admin.ModelAdmin):
    list_display = ('caption', 'type', 'value')

@admin.register(UserStatus)
class USAdmin(admin.ModelAdmin):
    list_display = ('caption',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('caption',)
