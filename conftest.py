"""
from ctypes.wintypes import tagMSG
from django.test import TestCase
import pytest
from typing import Dict, Tuple
from mixer.backend.django import mixer

# Internal
from integration.expert.models import Customer
from integration.expert.models import Step
from integration.expert.models import Category
from integration.expert.models import Inventory
from integration.customer.models import Coverage



@pytest.fixture
def create_customer(
    db,
    monkeypatch
):
    customer = mixer.blend(
        Customer,
        user=1,
        group=1,
        status=1,
        extra_data={"location": "cr6 a 47 a 40 bosque verde", "office_hours": "Lunes a Lunes 8am a 10pm"},
        is_active=1            
    )
    return customer


@pytest.fixture
def create_step(
    db,
    monkeypatch,
    create_customer
):
    step = mixer.blend(
        Step,
        step = "01_inicio",
        tag = "saludo",
        options = {"1": "Menu del dia", "2": "Productos", "3": "Combos"},
        is_active = 1,
        customer_id = create_customer.id
    )
    step = mixer.blend(
        Step,
        step = "02_recomendacion",
        tag = "productos",
        options = {"1": "gaseosa", "2": "pizzas", "3": "combos", "4": "asados"},
        is_active = 1,
        customer_id = create_customer.id
    )
    step = mixer.blend(
        Step,
        step = "03_otras_opciones",
        tag = "opciones",
        options = {"1": "Confirmar Pedido", "2": "Editar Pedido", "3": "Agregar Observacion"},
        is_active = 1,
        customer_id = create_customer.id
    )
    step = mixer.blend(
        Step,
        step = "04_recomendacion",
        tag = "cantidadproductos",
        options = {"1": "Confirmar Pedido", "2": "Editar Pedido", "3": "Agregar Observacion"},
        is_active = 1,
        customer_id = create_customer.id
    )
    return step


@pytest.fixture
def create_category(
    db,
    monkeypatch
):
    category = mixer.blend(
        Category,
        id = 1,
        category = "bebidas",
        is_active = 1
    )
    category = mixer.blend(
        Category,
        id = 2,
        category = "pizzas",
        is_active = 1
    )
    category = mixer.blend(
        Category,
        id = 3,
        category = "combos",
        is_active = 1
    )
    category = mixer.blend(
        Category,
        id = 4,
        category = "asados",
        is_active = 1
    )
    return category


@pytest.fixture
def create_inventory(
    db,
    monkeypatch,
    create_customer
):    
    inventory = mixer.blend(
        Inventory,
        id = 1,
        inventory = {"category": [{"name": "gaseosa", "products": ["Premio pet 500 - unidad a $2000", "Postobon pet 300 uva - unidad a $2000", "Postobon pet 500 manzana - unidad a $2000"]}, {"name": "jugo", "products": ["mora en agua - unidad a $3000", "mora en leche - unidad a $3000", "mandarina en agua - unidad a $3000"]}, {"name": "cerveza", "products": ["aguila - unidad a $4000", "pilsen - unidad a $4000", "club colombia - unidad a $4500"]}]},
        is_active = 1,
        category_id = Category.objects.get(id=1).id,
        customer_id = create_customer.id
    )
    inventory = mixer.blend(
        Inventory,
        id = 2,
        inventory = {"category": [{"name": "pizza personal", "products": ["Napolitana - unidad a $10000", "Mexicana - unidad a $10000", "Jamon y queso - unidad a $10000"]}, {"name": "pizza mediana", "products": ["pizza mediana paisa - unidad a $10000", "pizza mediana mexicana - unidad a $10000", "pizza mediana jamon y queso - unidad a $10000"]}, {"name": "Pizza grande", "products": ["pizza grande paisa - unidad a $20000", "pizza grande mexicana - unidad a $20000", "pizza grande jamon y queso - unidad a $20000", "pizza grande napolitana - unidad a $20000"]}]},
        is_active = 1,
        category_id = Category.objects.get(id=2).id,
        customer_id = create_customer.id
    )
    inventory = mixer.blend(
        Inventory,
        id = 3,
        inventory = {"category": [{"name": "combo 1", "products": ["combo 1 hamburguesa con papas y gaseosa - unidad a $16000"]}, {"name": "combo 2", "products": ["combo 2 perro con papas y gaseosa - unidad a $12000"]}]},
        is_active = 1,
        category_id = Category.objects.get(id=3).id,
        customer_id = create_customer.id
    )
    inventory = mixer.blend(
        Inventory,
        id = 4,
        inventory = {"category": [{"name": "asado 1", "products": ["asado 1 chuzo de res con papas - unidad a $22000"]}, {"name": "asado 2", "products": ["asado 2 chuzo de pollo con papas - unidad a $19000"]}]},
        is_active = 1,
        category_id = Category.objects.get(id=4).id,
        customer_id = create_customer.id
    )
    return inventory


@pytest.fixture
def create_coverage(
    db,
    monkeypatch,
    create_customer
):
    coverage = mixer.blend(
        Coverage,
        id = 1,
        coverage = {"coverage": [{"city": "medellin", "district": ["Buenos Aires", "Boston", "Centro"]}, {"city": "Envigado", "district": ["Palmas"]}]},
        customer_id = create_customer.id
    )
    return coverage
"""