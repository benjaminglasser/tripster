from django.urls import path
from . import views

urlpatterns = [
    path('', 
        views.home, name="home"),
    path('about/', 
        views.about, name="about"),
    # trips:
    path('trips/', 
        views.trips_index, name="index"),
    path('trips/<int:trip_id>', 
        views.trips_detail, name="detail"),
    path('trips/create/', 
        views.TripCreate.as_view(), name="trips_create"),
    path('trips/<int:pk>/update', 
        views.TripUpdate.as_view(), name='trips_update'),
    path('trips/<int:pk>/delete', 
        views.TripDelete.as_view(), name='trips_delete'),
    # stops:
    path('trips/<int:trip_id>/stop_create/',
        views.stop_create, name="stop_create"),
    path('stops/<int:stop_id>',
        views.stop_detail, name="stop_detail"),
    path('stops/<int:pk>/update',
        views.StopUpdate.as_view(), name='stop_update'),
    path('stops/<int:pk>/delete',
        views.StopDelete.as_view(), name='stop_delete'),
    path('stops/<int:stop_id>/add_photo/', 
        views.add_photo, name='add_photo'),
    #auth
    path('accounts/signup/',
        views.signup, name='signup'),



    # auth:
    # path('accounts/signup/', views.signup, name='signup'),
]
