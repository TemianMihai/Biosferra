from django.conf.urls import url,include
from .views import *
from . import views

urlpatterns = [
	url(r'^create-post/', create_post, name='post-create'),
    url(r'^post/(?P<slug>[-\w]+)/$', get_post, name='post-get'),
]