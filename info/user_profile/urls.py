from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^edit-profile/$', views.profile_detail, name='profile'),
    url(r'^/view-profile/(?P<slug>[^\.]+)/$', views.profile, name='profil'),
]