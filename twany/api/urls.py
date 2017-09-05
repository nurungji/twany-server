from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/v1/member/$', views.member_list),
    url(r'^api/v1/member/(?P<pk>[0-9]+)/$', views.member_detail),
    url(r'^api/v1/anniversary/$', views.YourView.get),
]
