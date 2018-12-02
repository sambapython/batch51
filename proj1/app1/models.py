# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name=models.CharField(max_length=60)
	cost=models.IntegerField()

	def get_data(self):
		return {"name":self.name, "cost":self.cost}
