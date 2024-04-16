from django.urls import path
from doctor_app.views import check_request,checked_request
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  # additional forms path
  path('lab_dashboard/', views.dis_lab_dash, name='lab_dashboard'),
  path('lab_dash_content/', views.dis_lab_dash_content, name='lab_dash_content'),
  path('lab_result/<str:lab_number>/', views.add_lab_result, name='add_lab_result'),
  path('dis_lab_result/', views.dis_lab_result, name='dis_lab_result'),
  path('check_request/',check_request ,name='check_request'),
  path('checked_request/<str:patient_id>/', checked_request, name='checked_request'),
path('profile/<int:user_id>/', views.tech_profile_update, name='tech_profile'),
path('show_tech_profile/',views.tech_profile, name='show_tech_profile')
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)