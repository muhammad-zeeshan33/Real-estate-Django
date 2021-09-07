from django.core import paginator
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from .choices import bedroom_choices, bathroom_choices, state_choices, garage_choice, type_choices, price_choices
def listings(request):
    listings= Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator =Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)    


def listing(request, listing_id):    
    listing = get_object_or_404(Listing, pk=listing_id)
    context={
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)



def search(request):
    queryset_list=Listing.objects.all()
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    if 'type' in request.GET:
        type = request.GET['type']
        if type:
            queryset_list = queryset_list.filter(type__iexact=type)
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(beds__lte=bedrooms)

    if 'garage' in request.GET:
        garage = request.GET['garage']
        if garage:
            queryset_list = queryset_list.filter(Garage__lte=garage)

    if 'bathrooms' in request.GET:
        bathrooms = request.GET['bathrooms']
        if bathrooms:
            queryset_list = queryset_list.filter(baths__lte=bathrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context={
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'type_choices': type_choices,
        'garage_choices': garage_choice, 
        'listings': queryset_list       
    }
    return render(request, 'listings/search.html', context)

def proptype(request):
    if 'orderby' in request.GET:
        orderby = request.GET['orderby']        
        if orderby == 'All':            
            listings = Listing.objects.order_by('-list_date')
        else: 
            listings = Listing.objects.order_by('-list_date').filter(type=orderby)               
        context={
            'listings' :  listings,
            'values': request.GET 
        }

        return render(request, 'listings/proptype.html', context)
    else:
        return render(request, 'listings/proptype.html')
