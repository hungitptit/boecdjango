# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Account)
admin.site.register(Address)
admin.site.register(Bank)
admin.site.register(Brand)
admin.site.register(Cart)
admin.site.register(Cartproduct)
admin.site.register(City)
admin.site.register(Comment)
admin.site.register(Company)
admin.site.register(Creditcard)
admin.site.register(Discountcode)
admin.site.register(District)
admin.site.register(Fullname)
admin.site.register(Nation)
admin.site.register(Normalorganizedsupplier)
admin.site.register(Officialsupplier)
admin.site.register(Order)
admin.site.register(Organizedsupplier)
admin.site.register(Payment)
admin.site.register(Paymenttype)
admin.site.register(Personalsupplier)
admin.site.register(Product)
admin.site.register(Productcategory)
admin.site.register(Productofsupplier)
admin.site.register(Productsubcategory)
admin.site.register(Rating)
admin.site.register(Shipment)
admin.site.register(Shipperunit)
admin.site.register(Supplier)
admin.site.register(Usertype)
admin.site.register(User)
admin.site.register(Viewedproduct)
admin.site.register(Ward)