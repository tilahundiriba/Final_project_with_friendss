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
    path('patients/', views.display_patients, name='display_patients'),
    path('refere_info/<int:discharge_no>/<str:patient_id>/', views.refere_info, name='refere_info'),
    path('general_report/', views.general_report, name='general_report'),
    # admin dashboard path
    path('dis_dash/', views.dis_dash, name='dis_dash'),
    path('dis_dash_content/', views.dis_dash_content, name='dis_dash_content'),
    path('user_log/', views.login_view, name='user_log'),
    path('index/', views.dis_index, name='index'),
    path('', views.dis_web_home, name='web_home'),
    path('dis_login2/', views.dis_login2, name='dis_login2'),
    path('save_data/<str:format>/', views.save_data, name='save_data'),
    path('dispaly_users/', views.display_users, name='display_users'),
    path('edit_staff/', views.edit_staff, name='edit_staff'),
    path('view_staff/<int:user_id>/', views.view_staff, name='view_staff'),
    path('deactivate/<int:user_id>/', views.deactivate, name='deactivate'),
    
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
