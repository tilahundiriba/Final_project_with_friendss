from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from .views import NotificationListView


# urlpatterns = [
#     path('generate-report-pdf/', generate_report_pdf, name='generate_report_pdf'),
#     # Add more URL patterns as needed
# ]
urlpatterns = [
    path('poster/', views.poster, name='poster'),
    # path('notifications/', NotificationListView.as_view(), name='notifications'),

    path('register/',views.createUserAccount, name='createUserAccount'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='admin_app/password_reset_form.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='admin_app/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='admin_app/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='admin_app/password_reset_complete.html'), name='password_reset_complete'),
    path('dis_base/', views.dis_base, name='dis_base'),
    # admin dashboard path
    path('dis_dash/', views.dis_dash, name='dis_dash'),
    path('dis_dash_content/', views.dis_dash_content, name='dis_dash_content'),
    path('user_log/', views.login_view, name='user_log'),
    path('index/', views.dis_index, name='index'),
    # path('user_registration/', views.dis_user_registration, name='user_registration'),
    path('web_home/', views.dis_web_home, name='web_home'),
    path('test_no_days/', views.bed_allocation_detail, name='dis_room'),
    path('dis_login2/', views.dis_login2, name='dis_login2'),
    path('save_data/<str:format>/', views.save_data, name='save_data'),
    path('dispaly_users/', views.display_users, name='display_users'),
    path('edit_staff/', views.edit_staff, name='edit_staff'),
    path('view_staff/<int:user_id>/', views.view_staff, name='view_staff'),
    path('deactivate/<int:user_id>/', views.deactivate, name='deactivate'),
    
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
