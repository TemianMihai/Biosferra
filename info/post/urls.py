from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
	url(r'^create-post/$', create_post, name='post-create'),
    url(r'^post/(?P<slug>[-\w]+)/$', get_post, name='post-get'),
    url(r'^post/(?P<slug>[\w-]+)/delete/$', delete_post, name='delete-post'),
    url(r'^post/(?P<slug>[\w-]+)/comanda/$', get_comanda, name='get-comanda'),
    url(r'^post/(?P<slug>[\w-]+)/finalizare-comanda/$', get_finalizare, name='get-finalizare'),
    url(r'^cosul-meu/$', produsele, name='produse'),
    url(r'^comenzile-mele/$', comanda, name='produse'),
    url(r'^comenzile-mele/(?P<slug>[\w-]+)/delete/$', delete_comanda, name='delete-comanda'),
]