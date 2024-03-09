from django.urls import path
from .views import SpeisekarteView
from pages.views import KundendatenView

urlpatterns = [
    path('speisekarte/', SpeisekarteView.as_view(), name='speisekarte'),
    path('kundendaten/', KundendatenView.as_view(), name='kundendaten'),
]
