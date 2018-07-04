from django.conf.urls import url
from . import views             # This line is new!
urlpatterns = [
    url(r'^$', views.index),    # This line has changed! 
    url(r'^register',views.register),
    url(r'^login', views.login),
    url(r'^logout',views.logout),
    url(r'^travels',views.travels),
    url(r'^home',views.travels),
    url(r'^destination/(?P<trip_id>\d+)$',views.destination),
    url(r'^addplan',views.addplan),
    url(r'^join/(?P<trip_id>\d+)$',views.join),
    url(r'^createtrip',views.createtrip),
]
#DjangoApps application