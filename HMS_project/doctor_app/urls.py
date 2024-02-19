from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('dis_dr_dash/', views.dis_dr_dash, name='dis_dr_dash'),
    path('dis_dr_dash_content/', views.dis_dr_dash_content, name='dis_dr_dash_content'),
    #path('patientOrder/', views.patientOrder, name='patientOrder'),
    path('patient_history/', views.dis_patient_history, name='patient_history'),
    path('about-appointment/', views.about_appointment, name='about-appointment'),
    path('add-appointment/', views.add_appointment, name='add-appointment'),
    path('edit-appointment/', views.edit_appointment, name='edit-appointment'),
    path('appointments/', views.dis_appointment, name='dis-appointment'),

] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

