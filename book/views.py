from django.shortcuts import render
from django.http import HttpResponse

import requests, yaml, datetime




key = 'AIzaSyAxcsY7PiyouoQ2okEbNEoqWgHrLR7yxts' # (maps.google.com) api simple key change to your own

def book(request):

	curtime = datetime.datetime.now()
	seconds = (curtime-datetime.datetime(1970,1,1)).total_seconds()
	print seconds
	if request.method == 'GET':
		print 'hello'
		print request.GET
		body = request.GET
		orig = body.__getitem__('from')
		dest = body.__getitem__('to')

		u='https://maps.googleapis.com/maps/api/distancematrix/json?origins='+orig+'&destinations='+dest+'&mode=driving&departure_time='+str(int(seconds))+'&traffic_model=pessimistic&language=en-GB&key='+key
		print u
		print requests.get(u).text
		map_data=yaml.safe_load(requests.get(u).text)
		if str(map_data['status'])=='OK':
			'''context_dict['duration'] = map_data['rows'][0]['elements'][0]['duration']['text']
			context_dict['price'] = int(float(map_data['rows'][0]['elements'][0]['distance']['value'])*0.001)
			context_dict['distance'] = map_data['rows'][0]['elements'][0]['distance']['text']
			context_dict['origin_addresses'] = map_data['origin_addresses'][0]
			context_dict['destination_addresses'] = map_data['destination_addresses'][0]'''
			return HttpResponse(map_data['rows'][0]['elements'][0]['duration']['text'])
		else:
			print 'empty'
	return HttpResponse("0")






def second(request):
	context_dict = {}

	if request.method == 'POST':
		body = request.POST
		orig = body.__getitem__('from')
		dest = body.__getitem__('to')

		context_dict['from'] = orig
		context_dict['to'] = dest

	return render(request, 'mymovetemplate.html', context_dict)
# Create your views here.


def index(request):
	return render(request, 'index.html')
# Create your views here.


def base(request):
	return render(request, 'base.html')

def aboutus(request):
	return render(request, 'about-us.html')

def becomeadriver(request):
	return render(request, 'becomeadriver.html')

def contact(request):
	return render(request, 'contact.html')

def faq(request):
	return render(request, 'faq.html')

def forpartner(request):
	return render(request, 'for-partner.html')

def howitworks(request):
	return render(request, 'how-it-works.html')

def movingguide(request):
	return render(request, 'moving-guide.html')

def privacy(request):
	return render(request, 'privacy.html')

def servicearea(request):
	return render(request, 'service-area.html')

def terms(request):
	return render(request, 'terms.html')

