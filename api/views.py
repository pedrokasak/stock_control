from django.shortcuts import render

import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import StoreSerializers
from store.models import Store


class StoreView(APIView):
    @staticmethod
    def get_store_in_json():
        queryset = Store.objects.all()
        data = []

        for store in queryset:
            store_data = {
                'name': store.name,
                'cnpj': store.cnpj,
                'email': store.email,
                'dateOfundation': store.date_of_fundation.strftime('%Y-%m-%d'),
                'address': store.address,
                'city': store.city,
                'state': store.state,
                'country': store.country
            }

            if store.image:
                store_data['image'] = store.image.url
            else:
                store_data['image'] = 'noting'

            data.append(store_data)

        return data

    def get(self, request):
        content = self.get_store_in_json()
        store_serializer = StoreSerializers(data=content, many=True)
        if store_serializer.is_valid():
            return Response(store_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(store_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
