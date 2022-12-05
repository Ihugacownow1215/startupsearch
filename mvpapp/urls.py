from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('avg-funding-by-person/<str:person_id>', views.average_funding),
    path('companies-by-person/<str:person_id>', views.companies),
    path('investors-by-company/<str:company_name>', views.investors),
]