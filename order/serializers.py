from rest_framework import serializers

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    coupon_code = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Order
        fields = ('user', 'total_amount', 'coupon_code')
