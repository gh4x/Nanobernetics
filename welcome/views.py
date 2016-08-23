from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'welcome/home.html', {'message': 'Nano Bernetics!'})
