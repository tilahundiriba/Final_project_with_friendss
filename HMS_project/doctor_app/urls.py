from django.urls import path
from receptionist_app.views import check_patient,check_patient_data
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('dis_dr_dash/', views.dis_dr_dash, name='dis_dr_dash'),
    path('dis_dr_dash_content/', views.dis_dr_dash_content, name='dis_dr_dash_content'),
    path('patient_history/', views.dis_patient_history, name='patient_history'),
    path('about-appointment/', views.about_appointment, name='about-appointment'),
    path('add-appointment/', views.create_appointment, name='add-appointment'),
    path('edit-appointment/', views.edit_appointment, name='edit-appointment'),
    path('appointments/', views.dis_appointment, name='dis-appointment'),

    path('perscriptions/', views.perscription, name='perscriptions'),
    path('add_perscription/', views.add_perscription, name='add_perscription'),
    path('edit_perscription/', views.edit_perscription, name='edit_perscription'),
    path('about_perscription/', views.about_perscription, name='about_perscription'),
    path('check_patient_data/', check_patient_data, name='check_patient_data'),
    path('check_patient/<str:patient_id>/', check_patient, name='check_patient'),
    path('add_lab/', views.add_lab, name='add_lab'),
    path('lab_tests/', views.dis_labtest, name='lab_tests'),
    path('profile/<int:user_id>/', views.updateProfile, name='profile'),
    path('profile_form/', views.dis_profile_form, name='profile_form'),
    path('profiles/', views.profiles, name='profiles'),


] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


