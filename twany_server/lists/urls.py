from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^members/$', views.member_list),
    url(r'^members/(?P<pk>[0-9]+)/$', views.member_detail),
]
