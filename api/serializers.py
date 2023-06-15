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

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.cnpj = validated_data.get('cnpj', instance.cnpj)
        instance.email = validated_data.get('email', instance.email)
        instance.date_of_fundation = validated_data.get('dateOfundation', instance.date_of_fundation)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance
