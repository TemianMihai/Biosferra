from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^edit-profile/$', views.profile_detail, name='profill'),
    url(r'^view-profile/(?P<slug>[^\.]+)/$', views.profile, name='profil'),
    url(r'^create-profile/$', views.create_profile, name='profiil'),
    url(r'^favoriti/$', views.favoriti, name='favorit'),
    url(r'^mesaje/$', views.mesaje, name='mesaje'),
    url(r'^mesaje-trimise/$', views.mesaje_trimise, name='mesaje-trimise')
]