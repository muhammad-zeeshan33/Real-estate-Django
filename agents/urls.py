from django.urls import path
from . import views

urlpatterns=[
    path('', views.agents, name='agents'),
    path('<int:agent_id>', views.agent, name='agent')

]