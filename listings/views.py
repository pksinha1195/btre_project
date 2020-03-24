from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .models import Listing
from .choices import *

# Create your views here.

def index(request):
    listings=Listing.objects.all().order_by('zipcode').filter(is_published=True)
    paginator=Paginator(listings,2)
    page_num = request.GET.get('page')
    page_listings=paginator.get_page(page_num)
    context={
        'listings':page_listings,
        'page' : page_num
    }
    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    listing=get_object_or_404(Listing,pk=listing_id)
    context={
        'listing' : listing 
    }
    return render(request, 'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    #keywords
    if 'keywords' in request.GET :
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains = keywords)
    #city
    if 'city' in request.GET :
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)
    #state
    if 'state' in request.GET :
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact = state)

    #bedrooms
    if 'bedrooms' in request.GET :
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte = bedrooms)

    #price
    if 'price' in request.GET :
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte = price)



            
    context ={
        'bedroom_choices': bedroom_choices,
        'price_choices' : price_choices,
        'state_choices' : state_choices,
        'listings' : queryset_list,
        'values':request.GET
    }
    return render(request, 'listings/search.html',context)