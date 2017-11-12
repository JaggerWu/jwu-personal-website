from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.index, name='jianwu'),
    url(r'^about_me', views.about_me, name='about_me'),
    url(r'^download_cv', views.download_cv, name='download_cv'),
]
