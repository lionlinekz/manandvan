from django.shortcuts import render
from django.http import HttpResponse
from book.forms import SearchForm, UserForm
from book.models import Search, Address, Van, Booking

import requests, yaml, datetime
from datetime import datetime as dt




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




def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
            'rango/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def second(request):
	context_dict = {}

	if request.method == 'POST':
		van_size = request.POST.get('van_size')
		helpers_required = request.POST.get('helpers_required')
		collection_postcode = request.POST.get('collection_postcode')
		collection_street_address = request.POST.get('collection_street_address')
		collection_city = request.POST.get('collection_city')
		collection_stairs = request.POST.get('collection_stairs')
		delivery_postcode = request.POST.get('delivery_postcode')
		delivery_street_address = request.POST.get('delivery_street_address')
		delivery_city = request.POST.get('delivery_city')
		delivery_stairs = request.POST.get('delivery_stairs')
		via1_postcode = request.POST.get('via1_postcode')
		via1_street_address = request.POST.get('via1_street_address')
		via1_city = request.POST.get('via1_city')
		via1_stairs = request.POST.get('via1_stairs')
		via2_postcode = request.POST.get('via2_postcode')
		via2_street_address = request.POST.get('via2_street_address')
		via2_city = request.POST.get('via2_city')
		via2_stairs = request.POST.get('via2_stairs')
		move_date = request.POST.get('move_date')
		move_time = request.POST.get('move_time')
		payg_item_description = request.POST.get('payg_item_description')
		customer_name = request.POST.get('customer_name')
		customer_email = request.POST.get('customer_email')
		customer_phone = request.POST.get('customer_phone')
		quote = request.POST.get('quote')
		description = request.POST.get('description')
		booking = create_booking(van_size, helpers_required, description, 50, customer_name, customer_email, customer_phone)
		collection = create_address(collection_postcode, collection_street_address, collection_city, collection_stairs)
		print collection
		delivery = create_address(delivery_postcode, delivery_street_address, delivery_city, delivery_stairs)
		print delivery
		booking.departure = collection
		booking.arrival = delivery
		if via1_postcode:
			stop1 = create_address(via1_postcode, via1_street_address, via1_city, via1_stairs)
			booking.stop1 = stop1
		if via2_postcode:
			stop2 = create_address(via2_postcode, via2_street_address, via2_city, via2_stairs)
			booking.stop2 = stop2
		booking.datetime = dt.strptime(move_date+" "+move_time, "%Y-%m-%d %H:%M")
		booking.save()
		booking.reference = 10000000 + booking.id
		booking.save()
		if request.user.is_authenticated():
			booking.user = request.user 
			booking.save()
			return render(request, 'booked.html', {'booking':booking})
		else:
			return render(request, 'booked.html', {'booking':booking})
	return render(request, 'mymovetemplate.html', context_dict)
# Create your views here.
def create_address(postcode, street_address, city, stairs):
	address = Address()
	address.postcode = postcode
	address.street = street_address
	address.city = city
	address.stairs = stairs
	address.save()
	return address

def create_booking(van_size, helpers_required, description, quote, name, email, phone):
	booking = Booking()
	booking.van_size = van_size
	booking.helping_guys = helpers_required
	booking.description = description
	booking.quote = quote
	booking.name = name
	booking.email = email
	booking.phone = phone
	return booking


def index(request):
	context_dict = {}
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if not form.is_valid():
			context_dict['errors'] = form.errors
			context_dict['form'] = SearchForm()
		else:
			search = form.save(commit=False)
			orig = search.from_postcode
			dest = search.to_postcode
			curtime = datetime.datetime.now()
			seconds = (curtime-datetime.datetime(1970,1,1)).total_seconds()
			u='https://maps.googleapis.com/maps/api/distancematrix/json?origins='+orig+'&destinations='+dest+'&mode=driving&departure_time='+str(int(seconds))+'&traffic_model=pessimistic&language=en-GB&key='+key
			map_data=yaml.safe_load(requests.get(u).text)
			if str(map_data['status'])=='OK':
				'''context_dict['duration'] = map_data['rows'][0]['elements'][0]['duration']['text']
				context_dict['price'] = int(float(map_data['rows'][0]['elements'][0]['distance']['value'])*0.001)
				context_dict['distance'] = map_data['rows'][0]['elements'][0]['distance']['text']
				context_dict['origin_addresses'] = map_data['origin_addresses'][0]
				context_dict['destination_addresses'] = map_data['destination_addresses'][0]'''
				#return HttpResponse(map_data['rows'][0]['elements'][0]['duration']['text'])
				return render(request, 'mymovetemplate.html', context_dict)
	return render(request, 'index.html', context_dict)
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

