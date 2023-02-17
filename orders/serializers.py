from rest_framework import serializers

from orders.models import OrderInfo


class OrderSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    status = serializers.CharField()

    class Meta:
        model = OrderInfo
        fields = "id date sum address".split()