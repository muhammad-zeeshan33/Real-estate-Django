from django.contrib import admin
from .models import Agent

class AgentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone' )
    list_display_links=('id','name')
    list_filter = ('name',)    
    search_fields = ('name', 'email', 'phone', 'description')
admin.site.register(Agent, AgentAdmin)

