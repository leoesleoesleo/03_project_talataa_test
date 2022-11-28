# Standard Library
import logging

# Django
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Internal
from integration.orders import services


logger = logging.getLogger(__name__)


class OrdersViews(
    APIView
):
    class InputSerializer(serializers.Serializer):
        dispatcher_id = serializers.IntegerField()
        date_order = serializers.CharField(
            max_length=10
        )

    class OutputSerializer(serializers.Serializer):
        date_order = serializers.CharField()
        status=serializers.ListField()
        orders=serializers.ListField()

    def get(self, request):
        try:            
            input_serializer = self.InputSerializer(data=request.data)
            input_serializer.is_valid(raise_exception=True)
            get_response = services.orders_dispatcher(
                **input_serializer.validated_data
            )
            validated_data = self.OutputSerializer(get_response).data
        except ValidationError:
            raise
        except Exception as e:
            logger.exception(f'customer-get: {e}')
            raise
        return Response(validated_data, status=status.HTTP_200_OK)

    class InputSerializerSave(serializers.Serializer):
        email = serializers.CharField(
            max_length=50
        )
        time_zone = serializers.IntegerField()
        direction = serializers.CharField(
            max_length=100
        )
        order = serializers.DictField()

    class OutputSerializerSave(serializers.Serializer):
        response = serializers.CharField()
        data=serializers.DictField()

    def post(self, request):
        try:
            input_serializer = self.InputSerializerSave(data=request.data)
            input_serializer.is_valid(raise_exception=True)
            get_response = services.customer_order(
                **input_serializer.validated_data
            )
            validated_data = self.OutputSerializerSave(get_response).data
        except ValidationError:
            raise
        except Exception as e:
            logger.exception(f'customer-post: {e}')
            raise
        return Response(validated_data, status=status.HTTP_201_CREATED)
