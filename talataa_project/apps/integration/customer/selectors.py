# Django
from django.db.models import QuerySet
from django.contrib.auth.models import User

# Internal
from integration.customer.models import Customer


def customer_email(
    *,
    email: str
) -> 'QuerySet[Customer]':
    return Customer.objects.filter(
        email=email
    ).last()
