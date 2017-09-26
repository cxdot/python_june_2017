from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index),
url(r'^amadon/buy/(?P<item_id>\d+)$', views.purchase),
url(r'^checkout$', views.checkout),
]
