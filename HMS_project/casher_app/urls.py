from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from doctor_app.views import check_payment_request,checked_payment_request 


urlpatterns = [
 
  path('discharges/', views.dis_discharge, name='discharges'),
  path('approve_discharges/<int:discharge_no>/', views.approve_discharge_request, name='approve_discharges'),
  path('add-payment/', views.add_payment, name='add-payment'),
  path('add-discharge/', views.add_discharge, name='add-discharge'),
  path('about-payment/<str:pay_number>/<str:patient_id>/', views.about_payment, name='about_payment'),
  path('payments/', views.dis_payment, name='dis_payment'),
  path('invoice/', views.invoice, name='invoice'),
  path('casher_dash/', views.casher_dash, name='casher_dash'),
  path('casher_dash_content/', views.casher_dash_content, name='casher_dash_content'),
  path('check_payment_request/',check_payment_request ,name='check_payment_request'),
  path('checked_payment_request/<str:patient_id>/', checked_payment_request, name='checked_payment_request'),
  path('profile/<int:user_id>/', views.casher_profile_update, name='update_chasher_profile'),
  path('profile/',views.profile, name='show_casher_profile'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)