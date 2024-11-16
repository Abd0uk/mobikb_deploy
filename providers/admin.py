from django.contrib import admin
from .models import Operator, CountryData, Network
# Register your models here.
admin.site.register(Operator)
admin.site.register(CountryData)
admin.site.register(Network)