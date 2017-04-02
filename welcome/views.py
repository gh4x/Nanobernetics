from django.shortcuts import render
from welcome.models import Event
from datetime import date


# Create your views here.
def home(request):
    return render(request, 'welcome/home.html', {'message': 'Nanobernetics!'})


def alpha(request):
    return render(request, 'welcome/alpha.html', {'message': 'Nanobernetics!'})


def index(request):
    today = date.today()
    past_events = Event.objects.filter(date__lt=today, visible__exact=True)
    upcoming_events = Event.objects.filter(date__gte=today, visible__exact=True)
    #upcoming_events = Event.objects.get(date>=today, visible=True)

    return render(request, 'welcome/index.html', {'past_events': past_events}, {'upcoming_events': upcoming_events})
