from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accessibility', views.accessibility, name='accessibility'),
    path('privacy', views.privacy, name='privacy'),
]
