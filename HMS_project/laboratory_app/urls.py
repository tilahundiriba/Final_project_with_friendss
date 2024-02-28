from django.urls import path
from . import views
urlpatterns = [
  # additional forms path
  path('', views.receptionist_dash, name=''),

] 