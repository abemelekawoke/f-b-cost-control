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
from menus.models import *
from items.models import *
# from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class AllMargins(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    menu_name = models.ForeignKey(Menus, on_delete=models.CASCADE, unique=True)
    profit_margin = models.DecimalField(max_digits=10, decimal_places=2, help_text='Profit margin in %')
    taxt_margin = models.DecimalField(max_digits=10, decimal_places=2, help_text='Tax margin in %')
    service_charge_margin = models.DecimalField(max_digits=10, decimal_places=2, help_text='Service charge margin in %')
    total_margin = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name_plural = "All margins"

    def __str__(self):
        return "%s" % self.menu_name

    def save(self, *args, **kwargs):
        self.total_margin = self.profit_margin+self.taxt_margin+self.service_charge_margin

        super(AllMargins, self).save(*args, **kwargs)