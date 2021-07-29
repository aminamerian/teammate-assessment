from django.urls import path
from assessment import views

urlpatterns = [
    path('', views.index, name="index"),
]
