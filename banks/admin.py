# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Bank, Branch


admin.site.register(Bank)
admin.site.register(Branch)