from django.urls import path
from receptionist_app.views import check_patient,check_patient_data
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('dis_dr_dash/', views.dis_dr_dash, name='dis_dr_dash'),
    path('view_notification/', views.test_notification, name='view_notification'),
    path('technician_list/', views.technician_list, name='technician_list'),
 
    path('dis_dr_dash_content/', views.dis_dr_dash_content, name='dis_dr_dash_content'),

    path('add_history/', views.add_history, name='add_history'),
    path('dis_history/', views.dis_history, name='dis_history'),
    path('edit_history/<int:history_no>/', views.edit_history, name='edit_history'),
    path('update_history/<int:history_no>/', views.update_history, name='update_history'),
   

    path('about-appointment/<int:app_number>/', views.about_appointment, name='about-appointment'),
    path('add-appointment/', views.create_appointment, name='add-appointment'),
    path('edit-appointment/<str:app_number>/', views.edit_appointment, name='edit-appointment'),
    path('appointments/', views.dis_appointment, name='dis-appointment'),
    path('perscriptions/', views.perscription, name='perscriptions'),
    path('add_perscription/', views.add_perscription, name='add_perscription'),
    path('edit_perscription/<str:prec_number>/', views.edit_perscription, name='edit_perscription'),
    path('about_perscription/<str:prec_number>/<str:patient_id>/', views.about_perscription, name='about_perscription'),
    path('check_patient_data/', check_patient_data, name='check_patient_data'),
    path('check_patient/<str:patient_id>/', check_patient, name='check_patient'),
    path('add_lab/', views.add_lab, name='add_lab'),
    path('lab_tests/', views.dis_labtest, name='lab_tests'),
    path('dis_lab_results/', views.dis_lab_results, name='dis_lab_results'),
    path('profile/<int:user_id>/', views.profile_update_doc, name='update_doctor_profile'),
    path('show_doctor_profile/',views.doc_profile, name='show_doctor_profile')



] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


