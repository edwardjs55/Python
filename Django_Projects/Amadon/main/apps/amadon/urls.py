from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index, name='amandon'),     # This line has changed!
url(r'^amadon/buy$',views.buy),
url(r'^reset$',views.reset),
url(r'^checkout$',views.checkout),
]