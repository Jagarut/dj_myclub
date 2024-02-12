from django.contrib import admin
from .models import Event, MyClubUser, Venue

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')    

# admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)
