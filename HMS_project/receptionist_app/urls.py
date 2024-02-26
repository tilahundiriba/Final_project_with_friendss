from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  # additional forms path
  path('receptionist_dash/', views.receptionist_dash, name='receptionist_dash'),
  path('dash_content/', views.receptionist_dash_content, name='receptionist_dash_content'),
  path('add-patient/', views.add_patient, name='add_patient'),
  path('edit-patient/<str:patient_id>/', views.edit_patient, name='edit-patient'),
  path('about_patient/', views.about_patient, name='about_patient'),
  path('dis_patient/', views.dis_patient, name='dis_patient'),
  path('dis_form/', views.dis_forms, name='dis_form'),
  path('delete_patient/', views.delete_patient, name='delete_patient'),
  path('update_patient/<str:patient_id>/', views.update_patient, name='update_patient'),


  #path('form/', views.form, name='form'),

  # path('form/', views.form, name='form'),

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)