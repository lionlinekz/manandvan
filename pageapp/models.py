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

class ChargesRelatedToJourney(models.Model):
    name = models.CharField(max_length=128, unique=True)
    
    stopping_fee = models.IntegerField(default=0) #Your fee for stopping at Via addresses on route to destination
    stopping_fee_na = models.IntegerField(default=0) #The national average

    flight_stairs_charge = models.IntegerField(default=0) #Your charge per flight of stairs per man
    flight_stairs_charge_na = models.IntegerField(default=0) #The national average

    dist_charge = models.IntegerField(default=0) #Your mileage charge per mile
    dist_charge_na_min = models.IntegerField(default=0) #National averages vary from
    dist_charge_na_max = models.IntegerField(default=0) #National averages vary to
    dist_charge_min_price = models.IntegerField(default=0) #Minimum Price

    free_running_dist = models.IntegerField(default=0) #Miles before running mileage added

    running_dist_charge = models.IntegerField(default=0) #Your running mileage charge per mile
    running_dist_charge_min_price = models.IntegerField(default=0) #Minimum Price

    out_of_hours_charge = models.IntegerField(default=0) #Your out of hours charge for bookings before 07.00 AM and after 19.00 PM
    out_of_hours_charge_na = models.IntegerField(default=0) #The national average

    #Discounts

    one_item_discount = models.IntegerField(default=0) #Your discount percentage for a 1 item move
    one_item_discount_na = models.IntegerField(default=0) #The national average

    student_discount = models.IntegerField(default=0) #Your discount percentage for student moves
    student_discount_na = models.IntegerField(default=0) #The national average

    london_c_zone_charge = models.IntegerField(default=0) #Your fee for entering the London congestion charge zone
    london_c_zone_daily_fee = models.IntegerField(default=0) #The daily fee charged by TfL is PP.pp per van entering the congestion charge zone
    london_c_zone_charge_max_price = models.IntegerField(default=0) #Maximum Price




    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

class AvailableVan(models.Model):
    driver_name = models.CharField(max_length=128, unique=True)
    van_type = models.CharField(max_length=128, unique=True)
    van_reg_number = models.CharField(max_length=128, unique=True)
    phone_number = models.CharField(max_length=30, unique=True)
    is_available = models.IntegerField(default=0)



    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.driver_name





