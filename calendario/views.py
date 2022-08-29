from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import EventForm
from django.http import HttpResponseRedirect

def calendario(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "Fernando"
    month = month.capitalize()
    # convertir mes de str a int
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)


    # defino calendario
    cal = HTMLCalendar().formatmonth(year, month_number)

    # llamo al año actual
    now = datetime.now()
    current_year = now.year

    # la hora actual
    time = now.strftime('%H:%M')



    return render(request,
        'calendario/calendario.html',{
        "name" : name,
        "year" : year,
        "month" : month,
        "month_number" : month_number,
        "cal" : cal,
        "current_year" : current_year,
        "time" : time,
        })


def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted=True    

    form = EventForm
    return render(request, 'eventos/add_event.html', {'form':form, 'submitted':submitted})

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'eventos/eventos.html', {'event_list' : event_list})

def mostrar_evento(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'eventos/mostrar-evento.html', {'event' : event})



def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'eventos/venues.html', {'venue_list' : venue_list})
