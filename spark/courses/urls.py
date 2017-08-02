from django.conf.urls import url
from spark.courses import views

urlpatterns = [
    url(r'^$', views.classes, name='classes'),
    url(r'^(?P<slug>[\w-]+)/$', views.classe_detail, name='classe_detail'),
    url(r'^(?P<slug>[\w-]+)/subscribe/$', views.subscribe, name='subscribe'),
    url(r'^(?P<slug>[\w-]+)/lecture/$', views.lecture, name='lecture'),
    url(r'^(?P<slug>[\w-]+)/lecture/(?P<pk>\d+)/$', views.lecture_detail, name='lecture_detail'),
    # url(r'^post/$', views.post, name='post'),
    # url(r'^like/$', views.like, name='like'),
    # url(r'^comment/$', views.comment, name='comment'),
    # url(r'^load/$', views.load, name='load'),
    # url(r'^check/$', views.check, name='check'),
    # url(r'^update/$', views.update, name='update'),
    # url(r'^remove/$', views.remove, name='remove_feed'),
    # url(r'^(\d+)/$', views.feed, name='feed'),
]
