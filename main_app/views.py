from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Trip, Stop, Photo
from .forms import StopForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#Constants:
S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'tripster-fg'


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

# trips:

@login_required
def trips_index(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trips/index.html', {'trips': trips})

@login_required
def trips_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    stop_form = StopForm()
    stops = Stop.objects.all()

    return render(request, 'trips/detail.html', {
        'trip': trip,
        'stop_form': stop_form,
        'stops': stops
    })


class TripCreate(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ['name', 'start_date', 'end_date',
              'start_location', 'end_location']
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TripUpdate(LoginRequiredMixin, UpdateView):
    model = Trip
    fields = ['name', 'start_date', 'end_date',
              'start_location', 'end_location']


class TripDelete(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = '/trips/'

# stops:

@login_required
def stop_create(request, trip_id):
    form = StopForm(request.POST)
    if form.is_valid():
        new_stop = form.save(commit=False)
        new_stop.trip_id = trip_id
        new_stop.save()
    return redirect('detail', trip_id=trip_id)

@login_required
def stop_detail(request, stop_id):
    stop = Stop.objects.get(id=stop_id)

    return render(request, 'stops/detail.html', {
        'stop': stop,
    })


class StopUpdate(LoginRequiredMixin, UpdateView):
    model = Stop
    fields = ['stop_name', 'stop_adress',
              'stop_city', 'stop_state', 'stop_date']


class StopDelete(LoginRequiredMixin, DeleteView):
    model = Stop
    success_url = '/trips/'


# auth:

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid Signup - Please Try Again'

    form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form, 'error_message': error_message})

#Photo:
@login_required
def add_photo(request, stop_id):
    photo_file= request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, stop_id=stop_id)
            photo.save()
        except Exception as error:
            print('An error occured uploading file to S3')
            print(error)
    return redirect('stop_detail', stop_id=stop_id)