from django.urls import path
from .views import *



app_name='traniee'



urlpatterns = [

    path('update/',update,name='update'),
    path('insert/',instert,name='insert'),
    path('list/',traniee_list,name='listTraniee'),
    path('delete/',delete,name='delete'),
    path('register/',Trainee_register,name='Trainee-register'),

]
