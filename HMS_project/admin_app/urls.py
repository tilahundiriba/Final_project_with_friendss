from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('test/', views.testing, name='test'),
    path('test_fees/', views.lab_test_payment, name='lab_test_payment'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('home/',views.home , name='home'),
    path('user_login/', views.user_login , name='user_login'),
    path('register/',views.signup, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='admin_app/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='admin_app/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='admin_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='admin_app/password_reset_complete.html'), name='password_reset_complete'),
    
]

#template_name='password_reset_form.html'
#template_name='password_reset_done.html'
#template_name='password_reset_confirm.html'
#template_name='password_reset_complete.html'