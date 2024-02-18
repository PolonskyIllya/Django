from django.urls import path
from . import views


urlpatterns = [
    path("", views.my_shop),
    path("second list", views.my_shop1),
]
