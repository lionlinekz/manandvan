from django.contrib import admin
from pageapp.models import HourlyRateForVanType,ChargesRelatedToJourney,AvailableVan

# Register your models here.
admin.site.register(HourlyRateForVanType)
admin.site.register(ChargesRelatedToJourney)
admin.site.register(AvailableVan)