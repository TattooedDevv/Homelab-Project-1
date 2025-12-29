from django.urls import path
from .views import home, health

urlpatterns = [
    path("", home),          # handles /api/
    path("health/", health), # handles /api/health/
]

