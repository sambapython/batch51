# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from app1.models import Product

# Create your views here.
from django.http import HttpResponse
def fun1(request):
	#[Product_dataobj,Product_dataobj]
	import pdb; pdb.set_trace()
	data =map(lambda pro_obj:pro_obj.get_data(), Product.objects.all())   
	#data = [pro_obj.get_data() for pro_obj in  Product.objects.all()]
	"""
	data = []
	for pro_obj in Product.objects.all():
		data.append(pro_obj.get_data())
	"""
	return HttpResponse(data)
