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
# from django_currentuser.middleware import (get_current_user, get_current_authenticated_user)
# from django_currentuser.db.models import CurrentUserField
from django.urls import reverse
from django.http import HttpResponse
from django.db.models import Q, Count, Avg, Sum
from menus.models import *
from setups.models import *
from items.models import *
from django.contrib import messages
# from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class MenuPortions(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    menu_name = models.ForeignKey(Menus, on_delete=models.CASCADE)
    item_name = models.ForeignKey(ItemLists, on_delete=models.CASCADE)
    item_amount = models.DecimalField(max_digits=25, decimal_places=2)
    item_cost = models.DecimalField(max_digits=25, decimal_places=2)
    
    class Meta:
        verbose_name_plural = "Menu portions"

    def __str__(self):
        return "%s" % self.menu_name

    def save(self, *args, **kwargs):
        cost = Items.objects.filter(name_id=self.item_name.id)

        self.item_cost = 0
        counts = 0
        for co in cost:
            counts+=1
            self.item_cost+=co.single_price_changed
        self.item_cost = self.item_amount * (self.item_cost/counts)

        mid = MenuPortions.objects.filter(menu_name=self.menu_name, item_name=self.item_name)

        # if mid.exists():
        #     raise ValueError("Item name already exists.")

        # mid = MenuPortions.objects.filter(Q(menu_name=self.menu_name.id) & Q(item_name=self.item_name.id))
        # if mid:
        #     return "Item name already exists."

        super(MenuPortions, self).save(*args, **kwargs)