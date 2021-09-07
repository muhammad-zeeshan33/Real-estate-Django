from django.shortcuts import render
from listings.models import Listing
from agents.models import Agent
from listings.choices import bedroom_choices, bathroom_choices, state_choices, type_choices, garage_choice, price_choices
def index(request):    
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:4]
    agents = Agent.objects.order_by('-hire_date').filter(is_mvp=True)[:3]
    context={
        'bedroom_choices': bedroom_choices,
        'bathroom_choices': bathroom_choices,
        'state_choices': state_choices,
        'price_choices': price_choices,
        'type_choices': type_choices,
        'garage_choices': garage_choice,
        'listings' : listings,
        'agents' : agents

        }
    return render(request,  'pages/index.html', context)

def about(request):
    agents = Agent.objects.order_by('-hire_date')[:3]
    mvps = Agent.objects.order_by('-hire_date').filter(is_mvp=True)[:1]
    context ={
        'agents': agents,
        'mvps': mvps
    }
    return render(request,  'pages/about.html', context)


def contact(request):
    return render(request, 'pages/contact.html')