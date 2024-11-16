from django.urls import path
from . import views


app_name = 'providers'


# temp = 'providers:operators'

urlpatterns = [
    path('', views.opeartors, name='operators'),
    path('<int:pk>', views.operator_detail, name = 'operator_detail'),
    path('get-country-data/<int:operator_id>/<str:country_code>/', views.get_country_data, name='get_country_data'),
]