from django.shortcuts import get_object_or_404, render
from .models import Event
# Create your views here.

def events(request):
    Events = Event.objects.all()
    data = {
        'Events': Events,
    }
    return render(request, 'webpages/events.html', data)

def single_event(request, id):
    event = get_object_or_404(Event, pk=id)
    data = {
        'event': event
    }
    return render(request, 'webpages/single.html', data)