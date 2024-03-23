from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('forgot_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('forgot_password/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('forgot_password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('forgot_password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
