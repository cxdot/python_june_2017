from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index, name='landing'),
url(r'^register$', views.register, name='register'),
url(r'^login$', views.login, name='login'),
url(r'^logout$', views.logout, name='logout'),
url(r'^travels$', views.travel_info, name='travels'),
url(r'^travels/add$', views.add_trip, name="add_trip"),
url(r'^trip$', views.trip, name="trip"),
url(r'^travels/destination/(?P<id>\d+)$', views.destination, name="destination"),
url(r'^joined_trips/(?P<id>\d+)$', views.join_trip, name="joined_trips"),
]
