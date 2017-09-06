from django.conf.urls import url

from . import couple_views

urlpatterns = [
    url(r'^api/v1/couple/$', couple_views.couple_list),
    url(r'^api/v1/couple/(?P<pk>[0-9]+)/$', couple_views.couple_detail),
]
