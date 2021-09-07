from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Agent
from listings.models import Listing
def agents(request):
    agents=Agent.objects.order_by('-hire_date')
    paginator =Paginator(agents, 6)
    page=request.GET.get('page')
    paged_agents=paginator.get_page(page)
    context={
        'agents': paged_agents
    }
    return render(request, 'agents/agents.html', context)

def agent(request, agent_id):
    listings = Listing.objects.order_by('-list_date').filter(agent=agent_id)
    agent = get_object_or_404(Agent, pk=agent_id)
    context = {
        "agent": agent,
        'listings': listings
        
    }
    return render(request, 'agents/agent.html', context)


