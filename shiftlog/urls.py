from django.urls import path
from . import views

app_name = 'shiftlog'

urlpatterns = [
    path('', views.home, name='home')
]