from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^upload/$', views.ProgressBarUploadView.as_view(), name='upload'),
]
