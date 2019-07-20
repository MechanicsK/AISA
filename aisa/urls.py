from django.urls import path 
from . import views

app_name = 'AISA'


urlpatterns = [path('',views.index, name='index'),
]
              
