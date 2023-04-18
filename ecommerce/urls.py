from django.urls import path
from ecommerce.views import *


urlpatterns = [
    path("", productpage),
    path("about/", aboutpage, name="about"),
    path("<int:id>/", singleProductView, name="single")
]