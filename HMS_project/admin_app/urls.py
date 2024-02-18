from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('test_fees/', views.lab_test_payment, name='lab_test_payment'),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('home/',views.home , name='home'),
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
    path('user_log/', views.login_view, name='user_log'),
    path('index/', views.dis_index, name='index'),
    path('user_registration/', views.dis_user_registration, name='user_registration'),
  # doctor dashboard path
   #doctor views path start here
    path('dis_dr_dash/', views.dis_dr_dash, name='dis_dr_dash'),
    path('dis_dr_dash_content/', views.dis_dr_dash_content, name='dis_dr_dash_content'),
    path('form/', views.form, name='form'),
    path('patient_history/', views.dis_patient_history, name='patient_history'),
    path('about-appointment/', views.about_appointment, name='about-appointment'),
    path('add-appointment/', views.add_appointment, name='add-appointment'),
    path('edit-appointment/', views.edit_appointment, name='edit-appointment'),
    path('appointments/', views.dis_appointment, name='dis-appointment'),

  # nurse views  path start here 
    path('nurse_dash/', views.nurse_dash, name='nurse_dash'),
    path('nurse_dash_content/', views.dis_nurse_dash_content, name='dis_nurse_dash_content'),
    path('medication/', views.dis_medication, name='medication'),
    path('vital_info/', views.dis_vital_info, name='vital_info'),
    path('add-room/', views.add_room, name='add_room'),
    path('edit-room/', views.edit_room, name='edit_room'),
    path('dis-room/', views.dis_room, name='dis_room'),
 

  # casher views  path start here
  path('bill/', views.dis_bill, name='bill'),
  path('add-payment/', views.add_payment, name='add-payment'),
  path('about-payment/', views.about_payment, name='about_payment'),
  path('payments/', views.dis_payment, name='dis_payment'),
  path('invoice/', views.invoice, name='invoice'),
  path('casher_dash/', views.casher_dash, name='casher_dash'),
  path('casher_dash_content/', views.casher_dash_content, name='casher_dash_content'),
  
  #receptionist views path start here
  path('receptionist_dash/', views.receptionist_dash, name='receptionist_dash'),
  path('dash_content/', views.receptionist_dash_content, name='receptionist_dash_content'),
  path('add-patient/', views.add_patient, name='add-patient'),
  path('edit-patient/', views.edit_patient, name='edit-patient'),
  path('about_patient/', views.about_patient, name='about_patient'),
  path('dis_patient/', views.dis_patient, name='dis_patient'),



 

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#template_name='password_reset_form.html'
#template_name='password_reset_done.html'
#template_name='password_reset_confirm.html'
#template_name='password_reset_complete.html'