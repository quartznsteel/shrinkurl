from django.urls import path

from . import views

urlpatterns = [
    path("<str:shorturl>", views.redirect_to_longurl),
    path("", views.submit_longurl),
]