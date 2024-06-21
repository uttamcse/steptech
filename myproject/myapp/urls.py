from django.urls import path
from . import views

urlpatterns = [
   
    path('hello/', views.hello ),
    path('users/', views.users),
    path('new_user', views.new_user),
    path('users/<int:id>', views.user_detail),    
]
