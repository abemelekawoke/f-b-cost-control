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

class Measurement(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250)
    value = models.PositiveIntegerField()
    
    class Meta:
        verbose_name_plural = "Measurements"

    def __str__(self):
        return "%s" % self.name

class ItemLists(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)    
    description = models.CharField(max_length=250, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Item lists"

    def __str__(self):
        return "%s" % self.name