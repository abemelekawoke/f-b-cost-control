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
# from django_currentuser.middleware import (
#     get_current_user, get_current_authenticated_user)
# from django_currentuser.db.models import CurrentUserField
from django.urls import reverse
from django.http import HttpResponse
# from smart_selects.db_fields import ChainedForeignKey
# Create your models here.

class Menus(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    menu_name = models.CharField(unique=True, max_length=100)
    menu_description = models.CharField(max_length=250)
    labor_cost = models.DecimalField(max_digits=25, decimal_places=2)
    utility_cost = models.DecimalField(max_digits=25, decimal_places=2)
    production_cost = models.DecimalField(max_digits=25, decimal_places=2)
    class Meta:
        verbose_name_plural = "Menus"

    def __str__(self):
        return "%s" % self.menu_name

    def save(self, *args, **kwargs):
        self.production_cost = self.labor_cost+self.utility_cost

        super(Menus, self).save(*args, **kwargs)