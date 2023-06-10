from rest_framework import serializers
from store.models import Store

class StoreSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cnpj = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=80)
    dateOfundation = serializers.DateField(format='%Y-%m-%d', source='date_of_fundation')
    image = serializers.CharField(required=False, read_only=True)
    address = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)


class StoreDeSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    cnpj = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=80)
    date_of_fundation = serializers.DateField(
        format='%Y-%m-%d', source='dateOfundation', required=False, allow_null=True)
    image = serializers.CharField(required=False, read_only=True)
    address = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=50)
    state = serializers.CharField(max_length=50)
    country = serializers.CharField(max_length=50)

    def create(self, validated_data):
        validated_data['date_of_fundation'] = validated_data.get('dateOfundation', None)
        store = Store.objects.create(**validated_data)
        return store