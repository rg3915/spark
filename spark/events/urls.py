from django.conf.urls import url
from spark.events import views

urlpatterns = [
    url(r'^$', views.events, name='events'),
    url(r'^post/$', views.post, name='post'),
    url(r'^like/$', views.like, name='like'),
    # url(r'^comment/$', views.comment, name='comment'),
    url(r'^load/$', views.load, name='load'),
    # url(r'^check/$', views.check, name='check'),
    # url(r'^update/$', views.update, name='update'),
    # url(r'^remove/$', views.remove, name='remove_feed'),
    # url(r'^(\d+)/$', views.feed, name='feed'),
]
