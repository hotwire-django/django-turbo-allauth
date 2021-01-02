# Django
from django.urls import include, path

urlpatterns = [path("account/", include("turbo_allauth.urls"))]
