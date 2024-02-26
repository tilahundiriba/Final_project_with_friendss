from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  # nurse views  path start here 
    path('nurse_dash/', views.nurse_dash, name='nurse_dash'),
    path('nurse_dash_content/', views.dis_nurse_dash_content, name='dis_nurse_dash_content'),
    path('medication/', views.dis_medication, name='medication'),
    path('vital_info/', views.add_vital_info, name='vital_info'),
    path('add-room/', views.add_room, name='add_room'),
    path('edit-room/', views.edit_room, name='edit_room'),
    path('dis-room/', views.dis_room, name='dis_room'),
    path('dis-vitals/', views.dis_vitals, name='dis_vitals'),
  
 
]