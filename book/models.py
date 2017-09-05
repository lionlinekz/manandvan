from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Search(models.Model):
    datetime = models.CharField(max_length=128)
    from_postcode = models.CharField(max_length=128)
    to_postcode = models.CharField(max_length=128)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.datetime
        
class Address(models.Model):
	postcode = models.CharField(max_length=128)
	street = models.CharField(max_length=128)
	city = models.CharField(max_length=128)
	stairs = models.CharField(max_length=10)

	def __unicode__(self):  #For Python 2, use __str__ on Python 3
		return self.postcode
	
class Van(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	car_model = models.CharField(max_length=20)
	licence_number = models.CharField(max_length=10)
	car_size = models.IntegerField(default=1)
	
class Booking(models.Model):
	reference = models.CharField(max_length=10, null=True)
	van_size = models.IntegerField(default=1)
	helping_guys = models.IntegerField(default=0)
	departure = models.ForeignKey(Address, related_name="departure")
	arrival = models.ForeignKey(Address, related_name="arrival")
	stop1 = models.ForeignKey(Address, related_name="stop1", null=True)
	stop2 = models.ForeignKey(Address, related_name="stop2", null=True)
	datetime = models.DateTimeField(null=True)
	description = models.CharField(max_length=1024)
	user = models.ForeignKey(User, blank=True, null=True)
	paid_status = models.BooleanField(default=False)
	quote = models.FloatField(default=0)
	status = models.CharField(max_length=20, default="Unconfirmed")
	van = models.ForeignKey(Van, blank=True, null=True)
	name = models.CharField(max_length=128)
	email = models.EmailField(max_length=128)
	phone = models.CharField(max_length=20)

	def __unicode__(self):  #For Python 2, use __str__ on Python 3
		return str(self.departure)+"->"+str(self.arrival)+" "+self.phone+" "+self.name


# Create your models here.
