from django.conf.urls import url

from . import user_views

urlpatterns = [
    url(r'^api/v1/user/$', user_views.user_list),
    url(r'^api/v1/user/(?P<pk>[0-9]+)/$', user_views.user_detail),
]
