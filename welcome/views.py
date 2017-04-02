from django.shortcuts import render
from welcome.models import Event


# Create your views here.
def home(request):
    return render(request, 'welcome/home.html', {'message': 'Nanobernetics!'})


def alpha(request):
    return render(request, 'welcome/alpha.html', {'message': 'Nanobernetics!'})


def index(request):
    return render(request, 'welcome/index.html', events=Event.objects )
