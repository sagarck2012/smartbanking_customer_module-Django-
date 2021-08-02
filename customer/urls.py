from django.urls import path
from . import views


app_name = 'customer'

urlpatterns =[
    path('add/', views.customer_add, name='customer_add'),
    # path('user_list/', views.user_list, name='user_list'),
    # path('user_edit/<int:pk>/', views.user_edit, name='user_edit'),
    # path('user_delete/<int:pk>/', views.user_delete, name='user_delete'),
    # path('user_profile/<int:pk>/', views.user_profile, name='user_profile'),

]

