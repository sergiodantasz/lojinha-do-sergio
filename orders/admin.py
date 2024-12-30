from django.contrib import admin

from orders import models


class ItemInline(admin.TabularInline):
    model = models.Item
    extra = 1


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    pass
