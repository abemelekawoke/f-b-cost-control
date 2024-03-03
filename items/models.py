from django.db import models
import os
# from import_export import resources
from django.db.models import Subquery, OuterRef
from django.db import connection
from django.utils import timezone
import datetime
from datetime import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
from django.urls import reverse
from django.http import HttpResponse
from setups.models import *
# from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class Items(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.ForeignKey(ItemLists, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, blank=True, null=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=25, decimal_places=2)
    # ingredient = models.DecimalField(max_digits=25, decimal_places=2, help_text='Amount used for menu portion')
    amount_changed = models.CharField(max_length=100)
    single_price = models.DecimalField(max_digits=25, decimal_places=2)
    single_price_changed = models.DecimalField(max_digits=25, decimal_places=2)
    total_price = models.DecimalField(max_digits=25, decimal_places=2)
    date_of_purchased = models.DateField()
    date_of_expired = models.DateField()
    batch_number = models.PositiveIntegerField(blank=True, null=True)
    barcode = models.PositiveIntegerField(blank=True, null=True)
    provider_phone_number = models.CharField(max_length=50, blank=True, null=True)
    provider_name = models.CharField(max_length=150, blank=True, null=True)
    provider_email = models.EmailField(blank=True, null=True)
    provider_website = models.CharField(max_length=120, blank=True, null=True)
    provider_address = models.TextField(max_length=250, blank=True, null=True)

    # created_at = models.DateField(auto_now=True)
    # created_by = CurrentUserField()
    # modified_at = models.DateTimeField(auto_now=True)
    # modified_by = CurrentUserField(related_name="mb1")

    # print(Items.objects.all())

    class Meta:
        verbose_name_plural = "Items"

    def __str__(self):
        return "%s" % self.name

    def save(self, *args, **kwargs):
        self.total_price = self.single_price * self.amount
        
        mid = Measurement.objects.get(id=self.measurement.id)

        if mid:
            self.amount_changed = self.amount * mid.value
            self.single_price_changed = self.single_price / mid.value

        # if mid.name=='Unit':
        #     self.amount_changed=self.amount
        #     self.single_price_changed = self.single_price
        # else:
        #     self.amount_changed=self.amount * 1000
        #     self.single_price_changed = self.single_price / 1000

        super(Items, self).save(*args, **kwargs)