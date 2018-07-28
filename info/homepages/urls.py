from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^legume/(?P<type>\w+)/$', views.anotimp_legume, name='legume'),
    url(r'^fructe/(?P<type>\w+)/$', views.anotimp_fructe, name='fructe'),
]