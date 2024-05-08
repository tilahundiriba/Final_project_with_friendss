from django.urls import path
from .import views



urlpatterns = [
  # nurse views  path start here 
    path('write_feedback/', views.write_feedback, name='write_feedback'),
    path('patient_dash/', views.patient_dash, name='patient_dash'),
    path('patient_info/', views.Patient_info, name='patient_info'),
    path('patient_info/<str:added_no>/', views.mark_as_read, name='mark_as_read'),

]