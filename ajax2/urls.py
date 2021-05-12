from django.urls import path
from . import views




urlpatterns = [
     #app_2
    path('', views.userPanel),
    path('ajax/get_user_info', views.getUserInfo, name = 'get_user_info'),
]
