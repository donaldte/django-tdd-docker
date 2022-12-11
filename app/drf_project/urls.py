
from django.contrib import admin
from django.urls import path, include
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.first_view, name='first_view'),
    path("", include("movies.urls")),
]
