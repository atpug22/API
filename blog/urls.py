from django.urls import path
from blog.views import *

urlpatterns=[
    path('',home,name="home"),
    path('map/',map,name="Map"),
    path('joke/',joke,name="Joke"),
]