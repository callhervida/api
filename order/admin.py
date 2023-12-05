from django.contrib import admin
from .models import Order, Coupon


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount')  # Display fields in the admin panel
    # Customize further as needed


class CouponAdmin(admin.ModelAdmin):
    list_display = ('expired', 'discount', 'code')  # Display fields in the admin panel
    # Customize further as needed


admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon, CouponAdmin)
