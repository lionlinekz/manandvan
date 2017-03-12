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


def addresslist(request, aim=None):
	context_dict = {}
	context_dict['target'] = str(aim)

	return render(request, 'addresslist.html', context_dict)

def calcdrivetime(orig,dest):
	curtime = datetime.datetime.now()
	seconds = (curtime-datetime.datetime(1970,1,1)).total_seconds()
	print orig+' haha'
	print dest+' haha'
	if len(orig)>0 and len(dest)>0:
		key = 'AIzaSyAxcsY7PiyouoQ2okEbNEoqWgHrLR7yxts'
		u='https://maps.googleapis.com/maps/api/distancematrix/json?origins='+orig+'&destinations='+dest+'&mode=driving&units=imperial&departure_time='+str(int(seconds))+'&traffic_model=pessimistic&language=en-GB&key='+key
		print u
		print requests.get(u).text
		map_data=yaml.safe_load(requests.get(u).text)
		if str(map_data['status'])=='OK':
			'''context_dict['duration'] = map_data['rows'][0]['elements'][0]['duration']['text']
			context_dict['price'] = int(float(map_data['rows'][0]['elements'][0]['distance']['value'])*0.001)
			context_dict['distance'] = map_data['rows'][0]['elements'][0]['distance']['text']
			context_dict['origin_addresses'] = map_data['origin_addresses'][0]
			context_dict['destination_addresses'] = map_data['destination_addresses'][0]'''
			return [map_data['rows'][0]['elements'][0]['duration']['text'],map_data['rows'][0]['elements'][0]['duration']['value'],map_data['rows'][0]['elements'][0]['distance']['text'],map_data['rows'][0]['elements'][0]['distance']['value']]
	return []

def booking(request):

	context_dict = {}
	if request.method == 'GET':
		body = request.GET
		context_dict['van_size']					= body.__getitem__('van_size')
		context_dict['helpers_required']			= body.__getitem__('helpers_required')
		orig = context_dict['collection_postcode'] 		= body.__getitem__('collection_postcode')
		context_dict['collection_street_address_1'] = body.__getitem__('collection_street_address')
		context_dict['collection_city'] 			= body.__getitem__('collection_city')
		context_dict['collection_stairs'] 			= body.__getitem__('collection_stairs')
		dest = context_dict['delivery_postcode'] 			= body.__getitem__('delivery_postcode')
		context_dict['delivery_street_address_1'] 	= body.__getitem__('delivery_street_address')
		context_dict['delivery_city']				= body.__getitem__('delivery_city')
		context_dict['delivery_stairs'] 			= body.__getitem__('delivery_stairs')
		context_dict['move_date'] 					= body.__getitem__('move_date')
		context_dict['move_time'] 					= body.__getitem__('move_time')
		context_dict['payg_item_description'] 		= body.__getitem__('payg_item_description')
		context_dict['customer_name'] 				= body.__getitem__('customer_name')
		context_dict['customer_email'] 				= body.__getitem__('customer_email')
		context_dict['customer_phone'] 				= body.__getitem__('customer_phone')

		aa = calcdrivetime(orig,dest)
		context_dict['drive_dist'] 				= aa[2]
		context_dict['drive_time'] 				= aa[0]
		


	return render(request, 'booking.html', context_dict)


