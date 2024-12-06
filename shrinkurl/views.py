from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import URLPair
import hashlib
from django.views.decorators.csrf import csrf_protect
from .forms import LongURLForm
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

def submit_longurl(request):
    if request.method == "POST":
        form = LongURLForm(request.POST)

        if form.is_valid():

            longurl = form.cleaned_data["longurl"]

            #generate short url hash
            shorturl = generate_short_hash(longurl)

            if(longurl == ''):
                return HttpResponse(status=204)

            #check if this shorturl is already in the DB before inserting
            if (URLPair.objects.filter(short_url = shorturl).exists()):
                return HttpResponse(status=404)

            #insert into database
            newUrlPair = URLPair.objects.create(long_url = longurl, short_url = shorturl)

            newURL = "www.shrinkurl.com/" + shorturl

            return render(request, "enjoy.html", {'newURL': newURL})
        
    else:
        form = LongURLForm()

    return render(request, "home.html", {"form": form})

def redirect_to_longurl(request, shorturl):

    #uri_pattern = request.resolver_match.url_name
    print(shorturl)

    if not (URLPair.objects.filter(short_url = shorturl).exists()):
        return HttpResponse(status=404)

    #retrieve the long url based on the short url
    foundURLPair = URLPair.objects.filter(short_url = shorturl).get()

    return HttpResponseRedirect(foundURLPair.long_url)

@csrf_protect
def insert_or_retrieve_url(request):
    if request.method == "POST":

        if 'longurl' in request.POST:
            longurl = request.POST['longurl']
        else:
            return HttpResponse(status=204)
        
        if(longurl == ''):
            return HttpResponse(status=204)

        #generate short url hash
        shorturl = generate_short_hash(longurl)

        #check if this shorturl is already in the DB before inserting
        if (URLPair.objects.filter(short_url = shorturl).exists()):
            return HttpResponse(status=404)

        #insert into database
        newUrlPair = URLPair.objects.create(long_url = longurl, short_url = shorturl)
        return HttpResponse(shorturl)

    #check if get request is empty before processing
    elif request.method == "GET":

        if 'shorturl' in request.GET:
            shorturl = request.GET['shorturl']
        else:
            return HttpResponse(status=204) 

        if not (URLPair.objects.filter(short_url = shorturl).exists()):
            return HttpResponse(status=404)

        #retrieve the long url based on the short url
        foundURLPair = URLPair.objects.filter(short_url = shorturl).get()
        return HttpResponse(foundURLPair.long_url)

def generate_short_hash(data):
    #Generates a short hash from the given data.

    # Use SHA-256 for security
    hash_object = hashlib.sha256(data.encode())
    hex_digest = hash_object.hexdigest()

    # Take the first 6 characters for a short hash
    return hex_digest[:6]

