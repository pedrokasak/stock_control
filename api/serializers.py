from rest_framework import serializers


class StoreSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cnpj = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=80)
    dateOfundation = serializers.DateField(format='%Y-%m-%d')
    image = serializers.CharField(required=False)
    address = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)
