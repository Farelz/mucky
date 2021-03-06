from django.conf.urls import url
from resturants.views import (
    RestaurantListView,
    RestaurantDetailView,
    RestaurantCreateView
)

from django.contrib.auth.views import LoginView


urlpatterns = [
    url(r'^$', RestaurantListView.as_view(), name='list'),
    url(r'^create/$', RestaurantCreateView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view(), name='detail'),
]
