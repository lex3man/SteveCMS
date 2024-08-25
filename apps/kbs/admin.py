from django.contrib import admin

from apps.kbs.models import Button, Keyboard

@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    list_display = ('caption', 'type')

@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ('caption', 'text', 'callback')
