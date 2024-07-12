from django.urls import path
from .views import fscohort

urlpatterns = [
    path('', fscohort),
]