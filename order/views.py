import os

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.template.loader import render_to_string

from order.models import Order
from order.serializers import OrderSerializer
from user.models import User


class OrderViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    serializer_class = OrderSerializer

    def create(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user  # Assuming user is authenticated
            total_amount = serializer.validated_data['total_amount']
            coupon_code = serializer.validated_data.get('coupon_code', '')

            order = Order.objects.create(user=user, total_amount=total_amount)
            if coupon_code:
                success, message = order.apply_coupon(coupon_code)
                if not success:
                    return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderInvoiceAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    # serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')  # Assuming you send order_id in the request

        try:
            order = Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=404)

        # serializer = self.serializer_class(order)

        # Generate and send email with order details as an invoice
        subject = f"Order Invoice #{order.id}"
        message = render_to_string('templates/order/order_email.html', {'order': order})
        recipient_email = order.user.email  # Assuming User model has an 'email' field

        from_email = os.getenv('EMAIL')

        send_mail(subject, message, from_email, [recipient_email])

        return Response('sent successfully', status=200)
