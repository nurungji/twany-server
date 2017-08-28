from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/member/$', views.member_list),
    url(r'^api/member/(?P<pk>[0-9]+)/$', views.member_detail),
]
