from django.shortcuts import render
from django.http import HttpResponse
from random import randint

import requests, yaml, datetime


key = 'AIzaSyAxcsY7PiyouoQ2okEbNEoqWgHrLR7yxts'

def pageapp(request):
	return HttpResponse("This is service page")

def checkpostcode(request, postcode=None):
	u='https://api.postcodes.io/postcodes/'+str(postcode)+'/validate'
	print u
	data=yaml.safe_load(requests.get(u, verify=False).text)
	if str(data['status'])=='200':
		return HttpResponse(str(data['result']))
	else:
		return HttpResponse("error")

def approxprice(request):
	s = str(randint(33,99))+'.'+str(randint(0,99))
	return HttpResponse(s)


