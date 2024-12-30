from django.contrib import admin

from products import models


class VariationInline(admin.TabularInline):
    model = models.Variation
    extra = 1


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [VariationInline]


@admin.register(models.Variation)
class VariationAdmin(admin.ModelAdmin):
    pass
