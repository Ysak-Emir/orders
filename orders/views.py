from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from orders.models import Order, Product
from orders.serializers import OrderSerializers

class OrderAPIView(APIView):
    serializer = OrderSerializers

    def post(self, request):
        order = Order(request)
        id = request.data['id']
        product = get_object_or_404(Product, id=id)