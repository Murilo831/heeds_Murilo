from django.urls import path
from .views import index, place, update, delete


urlpatterns = [
    path('', index, name='index'),
    path('place', place, name='place'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
]