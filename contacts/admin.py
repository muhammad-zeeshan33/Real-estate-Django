from django.contrib import admin
from .models import Contact , UserContact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone' )
    list_display_links=('id','name')
    list_filter = ('name',)    
    search_fields = ('name', 'email', 'phone',)
admin.site.register(Contact, ContactAdmin)

class UserContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject' )
    list_display_links=('id','name')
    list_filter = ('name',)    
    search_fields = ('name', 'email', 'subject')
admin.site.register(UserContact, UserContactAdmin)
