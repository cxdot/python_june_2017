from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^users$', views.index), 
url(r'^login$', views.login), 
url(r'^register$', views.register), 
url(r'^users/new$', views.register), 
]