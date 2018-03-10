from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='jianwu'),
    path('about_me', views.about_me, name='about_me'),
    path('cv', views.cv, name='JianWu_CV'),
    path('download_cv', views.download_cv, name='download_cv'),
]
