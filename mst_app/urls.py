from django.urls import path
from .views import mst_view

urlpatterns = [
    path('', mst_view),
]
