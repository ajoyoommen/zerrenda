from django.contrib import admin

from .models import List, Item


class ItemInline(admin.TabularInline):
    model = Item


class ListAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    inlines = [ItemInline]


admin.site.register(Item)
admin.site.register(List, ListAdmin)
