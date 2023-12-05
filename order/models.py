from django.db import models

from user.models import User


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.FloatField(blank=True, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, blank=True, null=True)

    STATUS_CHOICES = [
        ('Waiting for Confirmation', 'Waiting For Confirmation'),
        ('Order in Progress', 'Order in Progress'),
        ('Complete', 'Complete'),
    ]

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=True, null=True)

    def apply_coupon(self, coupon_code):
        try:
            coupon = Coupon.objects.get(code=coupon_code)
        except Coupon.DoesNotExist:
            return False, "Coupon code is not valid"

        # Check any additional conditions for the coupon here (e.g., expiration date, usage limit)
        # Add your validation logic based on your Coupon model fields

        discount_percentage = coupon.discount
        discount_amount = (discount_percentage / 100) * (self.total_amount)
        self.total_amount -= discount_amount  # Apply the discount
        self.save()
        return True, "Coupon applied successfully, discounted amount: {}".format(coupon.discount)