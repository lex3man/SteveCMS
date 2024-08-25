from django.contrib import admin

from apps.kbs.models import Button, Keyboard

class ButtonInline(admin.TabularInline):
    model = Button
    extra = 1

@admin.register(Keyboard)
class KeyboardAdmin(admin.ModelAdmin):
    list_display = ('caption', 'type')
    list_filter = ['type']
    inlines = [ButtonInline]
    exclude = ["buttons"]


# @admin.register(Button)
# class ButtonAdmin(admin.ModelAdmin):
#     list_display = ('caption', 'text', 'callback')
