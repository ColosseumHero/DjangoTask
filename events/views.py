from django.shortcuts import render
from django.http import HttpResponse
from .models import Event

def index(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

