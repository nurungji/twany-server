from django.conf.urls import url

from . import diary_views

urlpatterns = [
    url(r'^api/diary/$', diary_views.diary_list),
    url(r'^api/diary/(?P<pk>[0-9]+)/$', diary_views.diary_detail),
]
