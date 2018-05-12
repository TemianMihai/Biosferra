from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
	url(r'^create-post/', create_post, name='post-create'),
    url(r'^post/(?P<slug>[-\w]+)/$', get_post, name='post-get'),
    url(r'^post/(?P<slug>[\w-]+)/delete/$', delete_post, name='delete-post'),
]