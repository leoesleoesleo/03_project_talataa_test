# Standard Library
from datetime import datetime
from pyexpat import model

# Django
from django.db import models

# Internal
from integration.customer.models import DirectionCustomer


class Dispatcher(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.SmallIntegerField()
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	extra_data = models.JSONField(blank=True, default=dict)
	is_active = models.BooleanField(default=True)


class Orders(models.Model):
	id = models.AutoField(primary_key=True)
	dispatcher = models.ForeignKey(Dispatcher, on_delete=models.CASCADE)
	directioncustomer = models.ForeignKey(DirectionCustomer, on_delete=models.CASCADE)
	create_at = models.DateTimeField(auto_now_add=True)
	update_at = models.DateTimeField(auto_now=True)
	date_order = models.CharField(max_length=100)
	time_zone = models.IntegerField()
	status = models.SmallIntegerField(
		default=0,
		verbose_name='status'
	)
	orders = models.JSONField(blank=True, default=dict)
	is_active = models.BooleanField(default=True)
