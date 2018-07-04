from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),     # This line has changed!
url(r'^session_words$',views.index),
url(r'^addWord$',views.addWord),
url(r'^clear$',views.clear),
]
