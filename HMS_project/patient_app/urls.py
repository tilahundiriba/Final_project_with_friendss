from django.urls import path
from .import views



urlpatterns = [
  # nurse views  path start here 
    path('write_feedback/', views.write_feedback, name='write_feedback'),
    path('patient_dash/', views.patient_dash, name='patient_dash'),

]