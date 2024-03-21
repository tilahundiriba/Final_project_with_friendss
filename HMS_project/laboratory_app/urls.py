from django.urls import path
from doctor_app.views import check_request,checked_request
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  # additional forms path
  path('lab_dashboard/', views.dis_lab_dash, name='lab_dashboard'),
  path('lab_dash_content/', views.dis_lab_dash_content, name='lab_dash_content'),
  path('check_request/',check_request ,name='check_request'),
  path('checked_request/<str:patient_id>/', checked_request, name='checked_request'),
path('profile/<int:user_id>/', views.profile_update, name='profile'),
path('profile_show',views.profile, name='profile_show')
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)