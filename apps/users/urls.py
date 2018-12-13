from django.conf.urls import url
from . import views

urlpatterns = [
	# index -- get
	url(r'^$', views.index, name = 'index'), 
	# update  -- post
	# or show -- get
	url(r'^(?P<id>[0-9]+)/$', views.show, name = 'show'),
	# show -- get
	url(r'^(?P<id>[0-9]+)/edit/$', views.edit, name = 'edit'),
	# delete -- post
	url(r'^(?P<id>[0-9]+)/destroy/$', views.destroy, name = 'destroy'),
	# new -- get
	url(r'new/$', views.new, name = 'new'),
	# create -- post
	url(r'create/$', views.create, name = 'create')
]