from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('logga-in/', views.loginPage, name='login-page'),
    path('registrera-dig', views.registerPage, name='register-page'),
    path('logga-ut', views.logoutPage, name='logga-ut'),
    
    path('min-profil/', views.profilePage, name='profile-page'),
    
    path('återställ-lösenord/', auth_views.PasswordResetView.as_view(email_template_name='email_templates/reset-password-content.txt', template_name='password_reset_form.html'), name='password_reset'),
    path('återställ-lösenord/klar/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_form_done.html'), name='password_reset_done'),
    path('återställ/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='enter_new_password.html'), name='password_reset_confirm'),
    path('återställ/klar/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordchange_success.html'), name='password_reset_complete'),
]
