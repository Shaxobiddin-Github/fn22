from django.urls import path

from .views import index,detail

urlpatterns = [
    path('', index, name='home'),
    path('detail/<int:pk>/', detail, name='detail'),
    
]
