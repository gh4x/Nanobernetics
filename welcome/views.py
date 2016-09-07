from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'welcome/home.html', {'message': 'Nano Bernetics!'})


def alpha(request):
    return render(request, 'welcome/alpha.html', {'message': 'Nano Bernetics!'})


def index(request):
    return render(request, 'welcome/index.html', {'message': 'Nano Bernetics!'})