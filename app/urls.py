from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.land_list, name='land_list'),
    path('lease/<int:land_id>/', views.lease_land, name='lease_land'),
    path('my_leases/', views.my_leases, name='my_leases'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register'),
]
