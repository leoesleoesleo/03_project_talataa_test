# Standard Library
import logging

# Django
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

# Internal
from integration.customer.serializers import (
    CustomTokenObtainPairSerializer, CustomUserSerializer
)

logger = logging.getLogger(__name__)


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token': login_serializer.validated_data.get(
                        'access'
                    ),
                    'refresh-token': login_serializer.validated_data.get(
                        'refresh'
                    ),
                    'user': user_serializer.data,
                    'message': 'successful session'
                }, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect username or password'},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Incorrect username or password'},
                        status=status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.filter(id=request.data.get('username', 0))
        except ValidationError:
            raise
        except Exception as error:
            logger.exception("Error ::get:: %d", str(error))

        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message': 'Successfully closed session.'},
                            status=status.HTTP_200_OK)
        return Response({'error': 'This user does not exist.'},
                        status=status.HTTP_400_BAD_REQUEST)

