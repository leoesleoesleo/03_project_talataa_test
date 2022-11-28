# Django
from django.db.models import QuerySet

# Internal
from integration.orders.models import Orders, Dispatcher
from integration.customer.models import DirectionCustomer
from integration.orders.constants import IsActive


def orders_dispatcher(
    *,
    dispatcher_id: int,
    date_order: str
) -> 'QuerySet[Orders]':
    dispatcher = Dispatcher.objects.filter(
        pk=dispatcher_id
    ).last()
    return Orders.objects.filter(
        dispatcher_id=dispatcher.pk,
        date_order__contains=date_order
    )


def direction_customer(
    *,
    direction: str
) -> 'QuerySet[DirectionCustomer]':
    return DirectionCustomer.objects.filter(
        direction=direction
    ).last()


def dispatcher_list() -> 'QuerySet[Dispatcher]':
    return Dispatcher.objects.filter(
        is_active=IsActive.ACTIVE.value
    )
