from django.urls import path

from . import views

urlpatterns = [
    path('',views.f_upload)
]