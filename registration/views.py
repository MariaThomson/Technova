from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import registration
from .forms import RegistrationForm
# Create your views here.

def home(request):
    registrations  = registration.objects.all()
    context = {}
    context['registrations'] = registrations

    if request.POST:
        form = RegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return render(request,'home.html', context)
        else:
            form = RegistrationForm()
            context['form'] = form
    else:
        form = RegistrationForm(
            initial={
                'Name': '',
                'Event': '',
                'College': '',
                'Branch':'',
                'Semester':'',
            }
        )
        context['form'] = form
    
    return render(request,'home.html', context)
    # return HttpResponse("This is the home page")

def index_view(request):
    return HttpResponse("This is index page ha ha ha...")