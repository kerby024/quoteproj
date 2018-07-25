from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.display),
        url(r'^create$', views.create),
        url(r'^clear$', views.clear),
        url(r'^addfave/(?P<quoteid>\d+)', views.addfave),
        url(r'^removefave/(?P<quoteid>\d+)', views.removefave),
        url(r'^user/(?P<userid>\d+)', views.user),
]