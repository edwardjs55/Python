from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),     # This line has changed!
url(r'^signin$',views.signinPage ), # Open/ signin page
url(r'^signinValidate$',views.signin), #process, Logon validate
url(r'^register$',views.registerPage), # open the register page
url(r'^registerValidate$', views.register), # #process, Registration validate)
#url(r'^show/(?P<user_id>\d+)$', views.show), # use show/default page Uses user_id as Parm
url(r'^show$',views.show), # dummy show URL, add user_id later
url(r'^dashboard/admin$',views.adminDashboard),  # Open the Admin Dashboard
url(r'^dashboard$',views.dashboard), # Open User dashboard
url(r'^user/new$',views.addUser),  # admin add user screen
url(r'^user/edit$',views.userEdit), # User self edit screen
url(r'^user/edit/(?P<user_id>\d+)$',views.adminEdit), # Admin edit screeb
url(r'^usersave$',views.userSave), # user Self/edit save
url(r'^adminsave$',views.adminSave), # Admin Edit User save

]
