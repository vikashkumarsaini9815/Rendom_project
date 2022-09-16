from django.urls import path
from rendomapp import views


urlpatterns = [
    path('employe/', views.employe, name = 'employe'),
]