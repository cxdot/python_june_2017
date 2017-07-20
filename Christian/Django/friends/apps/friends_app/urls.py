from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^main$', views.index, name='landing'),
url(r'^register$', views.register, name='register'),
url(r'^login$', views.login, name='login'),
url(r'^logout$', views.logout, name='logout'),
url(r'^friends$', views.friends, name='friends'),
url(r'^user/(?P<id>\d+)$', views.user_profile, name='users'),
url(r'^add/(?P<id>\d+)$', views.add_friend, name='add_friend'),
url(r'^remove/(?P<id>\d+)$', views.remove_friend, name='remove_friend'),
]
