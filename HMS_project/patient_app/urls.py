from django.urls import path
from .import views



urlpatterns = [
  # nurse views  path start here 
    path('write_feedback/', views.write_feedback, name='wriet_feedback'),

]