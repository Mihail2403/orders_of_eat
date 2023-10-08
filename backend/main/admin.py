from django.contrib import admin

from .models import Worker, EatItem, Order, EatOfOrder

# Register your models here.
admin.site.register(Worker)
admin.site.register(EatItem)
admin.site.register(Order)
admin.site.register(EatOfOrder)