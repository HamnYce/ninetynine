from django.urls import path

from . import views

urlpatterns = [
        path('namegen', views.namegen, name='namegen')
]
