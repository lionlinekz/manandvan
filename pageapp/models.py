from __future__ import unicode_literals

from django.db import models

class HourlyRateForVanType(models.Model):
    name = models.CharField(max_length=128, unique=True)
    weekday_customer_loading_price = models.IntegerField(default=0)
    weekday_customer_loading_min_price = models.IntegerField(default=0)
    weekend_customer_loading_price = models.IntegerField(default=0)
    weekend_customer_loading_min_price = models.IntegerField(default=0)

    weekday_one_man_loading_price = models.IntegerField(default=0)
    weekday_one_man_loading_min_price = models.IntegerField(default=0)
    weekend_one_man_loading_price = models.IntegerField(default=0)
    weekend_one_man_loading_min_price = models.IntegerField(default=0)

    weekday_two_man_loading_price = models.IntegerField(default=0)
    weekday_two_man_loading_min_price = models.IntegerField(default=0)
    weekend_two_man_loading_price = models.IntegerField(default=0)
    weekend_two_man_loading_min_price = models.IntegerField(default=0)
    
    weekday_three_man_loading_price = models.IntegerField(default=0)
    weekday_three_man_loading_min_price = models.IntegerField(default=0)
    weekend_three_man_loading_price = models.IntegerField(default=0)
    weekend_three_man_loading_min_price = models.IntegerField(default=0)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name
