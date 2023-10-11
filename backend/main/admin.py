from django.contrib import admin

from .models import Worker, EatItem, Order, EatOfOrder


class EatsOfOrderInline(admin.TabularInline):
    model = EatOfOrder

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('id',)

@admin.register(EatItem)
class EatItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'components', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('worker', )
    list_filter = ('date',)
    inlines = [EatsOfOrderInline]

@admin.register(EatOfOrder)
class EatOfOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'eatItem')
    list_filter = ('eatItem', 'order')