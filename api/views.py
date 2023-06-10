from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.broker import StoreApp
from api.serializers import StoreSerializers, StoreDeSerializers
from store.models import Store


class StoreView(APIView):

    def get(self, request):
        store_app = StoreApp()
        content = store_app.get_store_info_and_return_in_json()
        store_serializer = StoreSerializers(data=content, many=True)
        if store_serializer.is_valid():
            return Response(store_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(store_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        body_request = request.data
        store_app = StoreApp()

        if isinstance(body_request, list):
            try:
                # Trata de uma lista de objetos
                store_serializer = StoreDeSerializers(data=body_request, many=True)
                if store_serializer.is_valid():
                    create_data = store_app.set_info_store(data=store_serializer.data)
                    if create_data:
                        return Response(store_serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(store_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                # Trata somente um objeto único
                store_serializer = StoreDeSerializers(data=body_request)
                if store_serializer.is_valid():
                    store_serializer.save()
                    return Response(store_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(store_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
