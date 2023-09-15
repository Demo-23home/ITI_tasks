from django.urls import path,include
from .views import *



urlpatterns = [
    path('traniees/', TranieeListCreateView.as_view(), name='traniee-list-create'),
    path('traniees/<int:pk>/', TranieeDetailView.as_view(), name='traniee-detail'),
]


