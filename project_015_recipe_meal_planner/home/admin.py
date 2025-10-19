from django.contrib import admin
from django.db.models import Sum

from .models import *

admin.site.register(Recipe)