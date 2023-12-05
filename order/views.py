from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from order.serializers import OrderSerializer


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
