from django.urls import path
from . import views

app_name = 'assistant'

# urlpatterns = [
#     path('', views.wizard, name='topics'),
#     path('get_cases/<int:topic_id>/', views.get_cases, name='get_cases'),
#     path('get_resolution/<int:case_id>/', views.get_resolution, name='get_resolution'),
# ]



urlpatterns = [
    path('', views.knowledge_wizard, name='topics'),
    path('get_cases/', views.get_cases, name='get_cases'),
    path('get_resolution/', views.get_resolution, name='get_resolution'),
]
