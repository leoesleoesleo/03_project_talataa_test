# Standard Library
from datetime import datetime
from pyexpat import model

# Django
from django.db import models


class Customer(models.Model):
	id = models.AutoField(primary_key=True)
	external_id = models.CharField(
		unique=True,
		max_length=50,
		verbose_name='external_id'
	)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	user = models.SmallIntegerField()
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=50, unique=True)
	extra_data = models.JSONField(blank=True, default=dict)
	is_active = models.BooleanField(default=True)


class DirectionCustomer(models.Model):
	id = models.AutoField(primary_key=True)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	direction = models.CharField(max_length=100)
