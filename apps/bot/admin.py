from django.contrib import admin
from .models import StaticMessages, Trigger, UserStatus, State

class MessagesInline(admin.StackedInline):
    model = StaticMessages
    fk_name = "state"

@admin.register(StaticMessages)
class SMAdmin(admin.ModelAdmin):
    list_display = ('caption', 'text')
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
                "classes": ["collapse"],
                "fields": ("state", "user_status", "trigger"),
            },
        ),
        (
            "Побочные эффекты",
            {
                "classes": ["collapse"],
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
    inlines = [MessagesInline]
