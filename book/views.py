from django.shortcuts import render

def index(request):
	return render(request, 'index.html')
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

