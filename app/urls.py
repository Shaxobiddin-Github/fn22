from django.urls import path

from .views import index,detail,register,user_login,user_logout,change_news,save_comments,send_message_to_email

urlpatterns = [
    path('', index, name='home'),
    path('detail/<int:pk>/', detail, name='detail'),
    path('register/',register, name='register'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('change/',change_news, name='change'),
    path('save_comments/<int:news_id>', save_comments, name='add_comments'),
    path('send_email/', send_message_to_email, name='send_email'),

    
]
