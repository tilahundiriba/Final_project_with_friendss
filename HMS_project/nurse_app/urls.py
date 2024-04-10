from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  # nurse views  path start here 
    path('nurse_dash/', views.nurse_dash, name='nurse_dash'),
    path('nurse_dash_content/', views.dis_nurse_dash_content, name='dis_nurse_dash_content'),
    path('add_medication/', views.add_medication, name='add_medication'),
    path('dis_medication/', views.dis_medication, name='dis_medication'),
    path('edit_medication/<int:med_no>/', views.edit_medication, name='edit_medication'),
    path('vital_info/', views.add_vital_info, name='vital_info'),
    path('add-room/', views.add_room, name='add_room'),
    path('edit-room/<int:bed_no>/', views.edit_room, name='edit_room'),
    path('dis-room/', views.dis_room, name='dis_room'),
    path('allocate_room/', views.allocate_room, name='allocate_room'),
    path('dis_allocate_bed/', views.dis_bed_allocation, name='dis_allocate_bed'),
    path('dis-vitals/', views.dis_vitals, name='dis_vitals'),
    path('profile/<int:user_id>/', views.nurse_profile_update, name='update_nurse_profile'),
    path('profile_show/',views.nurse_profile, name='show_nurse_profile')
  
 
]