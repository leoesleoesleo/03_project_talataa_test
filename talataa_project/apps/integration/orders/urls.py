# Django
from django.urls import path

# Internal
from integration.orders.view import OrdersViews

urlpatterns = [
    path(
        'request',
        OrdersViews.as_view(),
        name='orders'
    )
]
