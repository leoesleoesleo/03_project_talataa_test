# Django
from django.conf import settings

from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from integration.customer.view import Login, Logout


urlpatterns = [
    path(
        'orders/',
        include('integration.orders.urls')
    ),
    path(
        'admin/',
        admin.site.urls
    ),
    path(
        'logout/', Logout.as_view(), name='logout'
    ),
    path(
        'login/', Login.as_view(), name='login'
    ),
    path(
        'api/token/',
        TokenObtainPairView.as_view(), name='token_obtain_pair'
    ),
    path(
       'api/token/refresh/',
       TokenRefreshView.as_view(), name='token_refresh'
    ),
]
