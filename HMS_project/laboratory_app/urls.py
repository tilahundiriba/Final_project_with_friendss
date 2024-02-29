from django.urls import path
from . import views
urlpatterns = [
  # additional forms path
  path('lab_dashboard/', views.dis_lab_dash, name='lab_dashboard'),
  path('lab_dash_content/', views.dis_lab_dash_content, name='lab_dash_content'),

] 