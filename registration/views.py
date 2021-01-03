from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import registration

# Create your views here.

def home(request):
    registrations  = registration.objects.all()
    # todos  = Todo.objects.filter(date_added="")
    context = {}
    context['registrations'] = registrations
    return render(request,'home.html', context)
    # return HttpResponse("This is the home page")

def index_view(request):
    return HttpResponse("This is index page ha ha ha...")