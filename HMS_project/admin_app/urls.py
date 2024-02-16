from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('members/', views.members, name='members'),
    path('test/', views.testing, name='test'),
    path('test_fees/', views.lab_test_payment, name='lab_test_payment'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('home/',views.home , name='home'),
    path('user_login/', views.user_login , name='user_login'),
    path('register/',views.createUserAccount, name='createUserAccount'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='admin_app/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='admin_app/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='admin_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='admin_app/password_reset_complete.html'), name='password_reset_complete'),
    path('dis_login/', views.dis_login, name='dis_login'),
    path('dis_home/', views.dis_home, name='dis_home'),
    path('dis_homepage/', views.dis_homepage, name='dis_homepage'),
    path('dis_base/', views.dis_base, name='dis_base'),
    # admin dashboard path
    path('dis_dash/', views.dis_dash, name='dis_dash'),
    path('dis_dash_content/', views.dis_dash_content, name='dis_dash_content'),
  # doctor dashboard path
    path('dis_dr_dash/', views.dis_dr_dash, name='dis_dr_dash'),
    path('dis_dr_dash_content/', views.dis_dr_dash_content, name='dis_dr_dash_content'),
    path('form/', views.form, name='form'),
  # additional forms path
    path('bill/', views.dis_bill, name='bill'),
    path('medication/', views.dis_medication, name='medication'),
    path('patient_history/', views.dis_patient_history, name='patient_history'),
    path('user_registration/', views.dis_user_registration, name='user_registration'),
    path('vital_info/', views.dis_vital_info, name='vital_info'),

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#template_name='password_reset_form.html'
#template_name='password_reset_done.html'
#template_name='password_reset_confirm.html'
#template_name='password_reset_complete.html'