from django.conf.urls import url
from . import views

app_name ='tutorials'

urlpatterns =[
    url(r'^series/(?P<slug>[-\w]+)/$', views.tutorial_series_details ,name="tutorial_series_details"),
]
