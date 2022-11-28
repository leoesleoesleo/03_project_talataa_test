# Django
from django.test import TestCase

# Internal
from integration.customer.models import Customer, DirectionCustomer
from integration.orders.models import Dispatcher, Orders
from integration.orders import services as services_orders

class OrderModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Customer.objects.create(
            id=1,
            external_id=1,
            user=1,
            phone="300",
            email="test@gmail.com",
            extra_data={"location": "test", "office_hours": "test"},
            is_active=1
        )

        Customer.objects.create(
            id=2,
            external_id=2,
            user=2,
            phone="900",
            email="test2@gmail.com",
            extra_data={"location": "test2", "office_hours": "test2"},
            is_active=1
        )

        Customer.objects.create(
            id=3,
            external_id=3,
            user=3,
            phone="800",
            email="test3@gmail.com",
            extra_data={"location": "test3", "office_hours": "test3"},
            is_active=1
        )

        customer = Customer.objects.get(id=1)

        DirectionCustomer.objects.create(
            id=1,
            direction="cr 1a 11 11",
            customer_id=customer.pk
        )

        DirectionCustomer.objects.create(
            id=2,
            direction="cr 2a 22 22",
            customer_id=customer.pk
        )

        customer = Customer.objects.get(id=2)

        DirectionCustomer.objects.create(
            id=3,
            direction="cr 3a 33 33",
            customer_id=customer.pk
        )

        DirectionCustomer.objects.create(
            id=4,
            direction="cr 5a 55 55",
            customer_id=customer.pk
        )

        customer = Customer.objects.get(id=3)

        DirectionCustomer.objects.create(
            id=5,
            direction="cr 6a 66 66",
            customer_id=customer.pk
        )

        DirectionCustomer.objects.create(
            id=6,
            direction="cr 7a 77 77",
            customer_id=customer.pk
        )

        Dispatcher.objects.create(
            id=1,
            user=4,
            extra_data={"extra_data1": "test", "extra_data2": "test"},
            is_active=1
        )

        Dispatcher.objects.create(
            id=2,
            user=5,
            extra_data={"extra_data1": "test", "extra_data2": "test"},
            is_active=1
        )

        Dispatcher.objects.create(
            id=3,
            user=6,
            extra_data={"extra_data1": "test", "extra_data2": "test"},
            is_active=1
        )
        
        directioncustomer = DirectionCustomer.objects.get(id=1)
        dispatcher = Dispatcher.objects.get(id=1)

        Orders.objects.create(
            date_order="2022-11-28 16:59:59.524116",
            time_zone=8,
            status=0,
            orders={"test_order": "test_order"},
            is_active=1,
            directioncustomer_id=directioncustomer.pk,
            dispatcher_id=dispatcher.pk
        )

        directioncustomer = DirectionCustomer.objects.get(id=2)
        dispatcher = Dispatcher.objects.get(id=2)

        Orders.objects.create(
            date_order="2022-11-28 16:59:59.524116",
            time_zone=2,
            status=0,
            orders={"test_order2": "test_order2"},
            is_active=1,
            directioncustomer_id=directioncustomer.pk,
            dispatcher_id=dispatcher.pk
        )

    def test_customer_order(self):
        data_order = {
            "email": "test@gmail.com",
            "time_zone": 8,
            "direction": "cr 1a 11 11",
            "order": {
                "test_order":"test_order" 
            }
        }
        customer_order = services_orders.customer_order(
            email=data_order.get("email"),
            time_zone=data_order.get("time_zone"),
            direction=data_order.get("direction"),
            order=data_order.get("order")
        )

        assert customer_order.get("response") == "success"
        assert customer_order.get("data")["email"] == "test@gmail.com"
        assert customer_order.get("data")["dispatcher"] in (1, 2, 3)
    
    def test_orders_dispatcher(self):
        dispatcher = Dispatcher.objects.get(id=1)
        orders_dispatcher = services_orders.orders_dispatcher(
            dispatcher_id=dispatcher.pk,
            date_order="2022-11-28"
        )
        expected_response = {
            "date_order": "2022-11-28",
            "status": [
                0
            ],
            "orders": [
                {
                    "test_order": "test_order"
                }
            ]
        }
        assert orders_dispatcher == expected_response
