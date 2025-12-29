from django.contrib import admin
from django.urls import path, include
from api.views import home

urlpatterns = [
    path("", home),  # 👈 this makes http://127.0.0.1:8000/ work
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]

