from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('base/', views.kbase, name='kbase')
]