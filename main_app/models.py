from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Trip(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    start_location = models.CharField(max_length=100)
    end_location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'trip_id': self.id})


class Stop(models.Model):
    stop_name = models.CharField(max_length=100)
    stop_adress = models.CharField(max_length=100)
    stop_city = models.CharField(max_length=100)
    stop_state = models.CharField(max_length=100)
    stop_date = models.DateField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('stop_detail', kwargs={'stop_id': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for stop_id: {self.stop_id} @{self.url}"