from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index, name='landing'),
url(r'^register$', views.register, name='register'),
url(r'^login$', views.login, name='login'),
url(r'^logout$', views.logout, name='logout'),
url(r'^secrets$', views.secrets, name='secrets'),
url(r'^create_secret$', views.create_secret, name='create_secret'),
url(r'^popular_secrets$', views.popular_secrets, name='popular_secrets'),
url(r'^create_like/(?P<id>\d+)$', views.create_like, name='create_like'),
]
