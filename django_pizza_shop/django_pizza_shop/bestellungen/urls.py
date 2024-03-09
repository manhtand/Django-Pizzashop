from django.urls import path
from .views import BestellungListView

urlpatterns = [
    path('', BestellungListView.as_view(), name = 'bestellung_list')
]