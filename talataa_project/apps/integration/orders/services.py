# Standard Library
import logging
from datetime import datetime, timedelta
from typing import Dict, Union
import random

# Django
from django.db import transaction
from django.db.models import QuerySet

# Internal
from integration.orders.models import Orders, Dispatcher
from integration.customer.models import DirectionCustomer
from integration.orders.constants import StatusConstants, IsActive
from integration.orders import selectors
from integration.customer import selectors as selectors_customer


logger = logging.getLogger(__name__)


def orders_dispatcher(
    *,
    dispatcher_id: int,
    date_order: str
):  
    data_orders = selectors.orders_dispatcher(
        dispatcher_id=dispatcher_id,
        date_order=date_order
    )

    status = [row.status for row in data_orders]
    orders = [row.orders for row in data_orders]

    return {
        "date_order":date_order,
        "status": status,
        "orders": orders,
    }


def random_dispatchers(
    dispatchers: DirectionCustomer
) -> 'QuerySet[DirectionCustomer]':
    """
    Una vez tenemos guardada la información del pedido, debe asignarse a un 
    despachador (conductor) que tengamos dado de alta en el sistema de forma aleatoria
    """
    dispatcher_rows = [row.pk for row in dispatchers]
    id_dispatcher = random.choice([1,len(dispatcher_rows)])
    dispatcher = dispatchers[id_dispatcher-1]
    return dispatcher


def date_order_hour(
    time_zone:int
)-> str:
    """
    Franja de hora seleccionada para la entrega 
    (variable, pueden ser desde franjas de 1h hasta de 8h)
    """
    now = datetime.now()
    return now + timedelta(hours=time_zone)


def customer_order(
    *,
    email: str,
    time_zone: int,
    direction: str,
    order: Dict
):
    validate_email = selectors_customer.customer_email(
        email=email
    )

    # validar que el email exista
    if validate_email:
        directioncustomer = selectors.direction_customer(
            direction=direction
        )

        dispatchers = selectors.dispatcher_list()

        dispatcher = random_dispatchers(
            dispatchers=dispatchers
        )
        
        date_order = date_order_hour(
            time_zone=time_zone
        )
        
        save_customer_order(
            time_zone=time_zone,
            date_order=date_order,
            order=order,
            directioncustomer=directioncustomer,
            dispatcher=dispatcher
        )

        return {
            "response": "success",
            "data": {
                "email":email,
                "deliver_date":date_order,
                "date_order":datetime.now(),
                "dispatcher":dispatcher.pk
            }
        }

    else:
        return {
            "response": "email not exist",
            "data": {}
        }


@transaction.atomic()
def save_customer_order(
    *,
    time_zone: int,
    date_order: datetime,
    order: Dict,
    directioncustomer: DirectionCustomer,
    dispatcher: Dispatcher
) -> Union[None]:
    Orders(
        create_at=datetime.now(),
        update_at=datetime.now(),
        date_order=date_order,
        time_zone=time_zone,
        status=StatusConstants.PENDING.value,
        orders=order,
        is_active=IsActive.ACTIVE.value,
        directioncustomer=directioncustomer,
        dispatcher=dispatcher
    ).save()
