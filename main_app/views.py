from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# trips:


def trips_index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.html', {'trips': trips})


def trips_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trips/detail.html', {'trip': trip})


class TripCreate(CreateView):
    model = Trip
    fields = ['name', 'start_date', 'end_date',
              'start_location', 'end_location']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


class TripUpdate(UpdateView):
    model = Trip
    fields = ['name', 'start_date', 'end_date',
              'start_location', 'end_location']


class TripDelete(DeleteView):
    model = Trip
    success_url = '/trips/'

# auth:


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')
