from django.urls import path
from . import views

urlpatterns = [
     path("", views.my_product),
     path("second list", views.my_product1),
]