from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^result$',views.result),
    url(r'^survey/process$',views.process),
    url(r'^reset$',views.reset)
]
