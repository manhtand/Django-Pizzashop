from django.urls import path
from django_pizza_shop.pizza_api import views

urlpatterns = [
    path('view/', views.PizzaApiView.as_view()),
]