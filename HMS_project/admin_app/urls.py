from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('poster/', views.poster, name='poster'),
    path('approve_departures/', views.approve_departure, name='approve_departure'),
    path('add_service/', views.add_service, name='add_service'),
    path('dis_service/', views.dis_service, name='dis_service'),
    path('edit_service/<str:service>/', views.edit_service, name='edit_service'),
    path('seen_notifications/<int:id>/', views.mark_notification_as_seen, name='seen_notifications'),
    path('admin_profile/', views.admin_profile, name='admin_profile'),
    path('admin_profile_update/<int:user_id>/', views.profile_update_admin, name='admin_profile_update'),

    path('register/',views.createUserAccount, name='createUserAccount'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='admin_app/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='admin_app/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='admin_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='admin_app/password_reset_complete.html'), name='password_reset_complete'),
    path('dis_base/', views.dis_base, name='dis_base'),
    path('add_report/', views.add_report, name='add_report'),
    path('refere_info/<int:discharge_no>/<str:patient_id>/', views.refere_info, name='refere_info'),
    path('general_report/', views.general_report, name='general_report'),
    # admin dashboard path
    path('dis_dash/', views.dis_dash, name='dis_dash'),
    path('dis_dash_content/', views.dis_dash_content, name='dis_dash_content'),
    path('user_log/', views.login_view, name='user_log'),
    path('index/', views.dis_index, name='index'),
    path('', views.dis_web_home, name='web_home'),
    path('dis_login2/', views.dis_login2, name='dis_login2'),
    path('dis_appointments/', views.dis_appointment, name='dis_appointment'),
    path('dis_histories/', views.dis_history, name='history'),
    path('dis_prescriptions/', views.perscription, name='dis_perscription'),
    path('dis_vitals/', views.dis_vitals, name='vitals'),
    path('dis_labs/', views.dis_lab_result, name='laboratories'),
    path('patients/', views.dis_patient, name='patient'),
    path('payments/', views.dis_payment, name='payments'),
    path('departed/', views.dis_discharge, name='departed'),
    path('medications/', views.dis_medication, name='medications'),
    path('save_data/<str:format>/', views.save_data, name='save_data'),
    path('dispaly_users/', views.display_users, name='display_users'),
    path('edit_staff/', views.edit_staff, name='edit_staff'),
    path('view_staff/<int:user_id>/', views.view_staff, name='view_staff'),
    path('deactivate/<int:user_id>/', views.deactivate, name='deactivate'),
    path('activate/<int:user_id>/', views.activate, name='activate'),
    path('delete_medication', views.delete_medication, name='delete_medication'),
    path('delete_labratory/', views.delete_labratory, name='delete_labratory'),
    path('delete_patient/', views.delete_patient, name='admin_delete_patient'),
    path('delete_vital/', views.delete_vital, name='delete_vital'),
    path('delete_appointment/', views.delete_appointment, name='delete_appointment'),
    path('delete_history/', views.delete_history, name='delete_history'),
    path('delete_prescription/', views.delete_prescription, name='delete_prescription'),
    path('delete_discharge/', views.delete_discharge, name='delete_discharge'),
    path('delete_payment/', views.delete_payment, name='delete_payment'),



    
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
