from django.urls import path

from .views import index,detail,register,user_login,user_logout

urlpatterns = [
    path('', index, name='home'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('register/',register, name='register'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    # path('search/', search, name='search'),

    
]
