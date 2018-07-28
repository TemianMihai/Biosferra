from django.conf.urls import url
from .views import *
from . import views

urlpatterns = [
	url(r'^create-post/$', create_post, name='post-create'),
    url(r'^post/(?P<slug>[-\w]+)/$', get_post, name='post-get'),
    url(r'^post/(?P<slug>[\w-]+)/delete/$', delete_post, name='delete-post'),
    url(r'^post/(?P<slug>[\w-]+)/comanda/$', get_comanda, name='get-comanda'),
    url(r'^post/(?P<slug>[\w-]+)/finalizare-comanda/$', get_finalizare, name='get-finalizare'),
    url(r'^cosul-meu/(?P<slug>[\w-]+)/delete/$', delete_cos, name='delete-anunt-cos'),
    url(r'^cosul-meu/$', produsele, name='produse'),
    url(r'^comenzile-mele/$', comanda, name='produse'),
    url(r'^view-profile/(?P<slug>[^\.]+)/comenzi-primite/delete/$', delete_comanda, name='delete-comanda'),
    url(r'^view-profile/(?P<slug>[^\.]+)/comenzi-primite/$', get_comandap, name='get-comandap'),
    url(r'^view-profile/(?P<slug>[^\.]+)/comenzi-trimise/$', get_comandat, name='get-comandat')

]