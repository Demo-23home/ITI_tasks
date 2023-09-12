from django.urls import path
from .views import *


app_name = 'instructor'



urlpatterns = [

    path('update/',update,name='update'),
    path('insert/',instert,name='insert'),
    path('list/',list,name='list'),
    path('delete/',delete,name='delete'),
    path('register/',register,name='register'),

]
