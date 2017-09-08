from django.conf.urls import url

from . import couple_views

urlpatterns = [
    url(r'^api/v1/couple/$',
        couple_views.CoupleList.as_view(),
        name=couple_views.CoupleList.name),
    url(r'^api/v1/couple/(?P<pk>[0-9]+)/$',
        couple_views.CoupleDetail.as_view(),
        name=couple_views.CoupleDetail.name),
    url(r'^$',
        couple_views.ApiRoot.as_view(),
        name=couple_views.ApiRoot.name),

]
