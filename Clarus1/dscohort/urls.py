from django.urls import path
from .views import dshome

urlpatterns = [
    path('', dshome)
]
