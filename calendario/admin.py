from django.contrib import admin
from .models import Venue
from .models import Event
from .models import Usuario

# Register your models here.

#admin.site.register(Venue)
#admin.site.register(Event)
admin.site.register(Usuario)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = ('name', 'event_date', 'description',)
    list_display = ('name', 'event_date',)
    ordering = ('name',)
    search_fields = ('name', 'event_date',)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    fields = ('name', 'address')
    list_display = ('name', 'address')
    list_filter = ('name', 'address')
    ordering = ('name',)