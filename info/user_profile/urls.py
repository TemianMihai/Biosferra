from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^edit-profile/$', views.profile_detail, name='profill'),
    url(r'^create-profile/$', views.create_profile, name='profiil'),
    url(r'^create-profile/finalizare/$', views.get_profilf, name='get-profilt'),
    url(r'^favoriti/$', views.favoriti, name='favorit'),
    url(r'^mesaje/$', views.mesaje, name='mesaje'),

    url(r'^mesaje-trimise/$', views.mesaje_trimise, name='mesaje-trimise'),
    url(r'^view-profile/(?P<slug>[^\.]+)/mesaje-trimise/$', views.get_mesajet, name='get-mesajt'),
    url(r'^view-profile/(?P<slug>[^\.]+)/$', views.profile, name='profil'),
    url(r'^trimite-mesaje/(?P<slug>[\w-]+)/$', views.mesaj_profile, name='measaj-user')
]