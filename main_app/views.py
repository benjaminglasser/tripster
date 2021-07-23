from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trip, Stop
from .forms import StopForm


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
    stop_form = StopForm()
    stops = Stop.objects.all()

    return render(request, 'trips/detail.html', {
        'trip': trip,
        'stop_form': stop_form,
        'stops': stops
    })


class TripCreate(CreateView):
    model = Trip
    fields = ['name', 'start_date', 'end_date',
              'start_location', 'end_location']

    def form_valid(self, form):

        form.instance.user = self.request.user
        return super().form_valid(form)


class TripUpdate(UpdateView):
    model = Trip
    fields = ['name', 'start_date', 'end_date',
              'start_location', 'end_location']


class TripDelete(DeleteView):
    model = Trip
    success_url = '/trips/'

# stops:


def stop_create(request, trip_id):
    form = StopForm(request.POST)
    if form.is_valid():
        new_stop = form.save(commit=False)
        new_stop.trip_id = trip_id
        new_stop.save()
    return redirect('detail', trip_id=trip_id)


def stop_detail(request, stop_id):
    stop = Stop.objects.get(id=stop_id)

    return render(request, 'stops/detail.html', {
        'stop': stop,
    })


class StopUpdate(UpdateView):
    model = Stop
    fields = ['stop_name', 'stop_adress',
              'stop_city', 'stop_state', 'stop_date']


class StopDelete(DeleteView):
    model = Stop
    success_url = '/trips/'

# auth:


def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')
