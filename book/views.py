from django.shortcuts import render
from django.http import HttpResponse

import requests, yaml




key = 'AIzaSyAxcsY7PiyouoQ2okEbNEoqWgHrLR7yxts' # (maps.google.com) api simple key change to your own

def book(request):

	context_dict = {}

	if request.method == 'POST':
		print 'hello'
		print request.POST
		body = request.POST
		orig = body.__getitem__('from')
		dest = body.__getitem__('to')
		date = body.__getitem__('date')

		u='https://maps.googleapis.com/maps/api/distancematrix/json?origins='+orig+'&destinations='+dest+'&mode=driving&language=en-GB&key='+key

		

		if date == '112358':
			map_data=yaml.safe_load(requests.get(u).text)
			if str(map_data['status'])=='OK':
				context_dict['duration'] = map_data['rows'][0]['elements'][0]['duration']['text']
				context_dict['price'] = int(float(map_data['rows'][0]['elements'][0]['distance']['value'])*0.001)
				context_dict['distance'] = map_data['rows'][0]['elements'][0]['distance']['text']
				context_dict['origin_addresses'] = map_data['origin_addresses'][0]
				context_dict['destination_addresses'] = map_data['destination_addresses'][0]
				return render(request, 'search-results.html', context_dict)

		
	else:
		print 'empty'
	return render(request, 'index.html')


'''{u'status': u'OK', u'rows': [{u'elements': [{u'duration': {u'text': u'3 hours 45 mins', u'value': 13509}, u'distance': {u'text': u'347 km', u'value': 346652}, u'status': u'OK'}]}], u'origin_addresses': [u'Boston, MA, USA'], u'destination_addresses': [u'New York, NY, USA']}'''








def index(request):
	return render(request, 'mymove.html')
# Create your views here.



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

