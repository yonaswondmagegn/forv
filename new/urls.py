from django.urls import path
from .views import newView


urlpatterns = [
    path('',newView,name='newView')
]