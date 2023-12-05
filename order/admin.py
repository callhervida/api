from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount')  # Display fields in the admin panel
    # Customize further as needed


admin.site.register(Order, OrderAdmin)
