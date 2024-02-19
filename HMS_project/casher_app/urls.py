from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 
  path('bill/', views.dis_bill, name='bill'),
  path('add-payment/', views.add_payment, name='add-payment'),
  path('about-payment/', views.about_payment, name='about_payment'),
  path('payments/', views.dis_payment, name='dis_payment'),
  path('invoice/', views.invoice, name='invoice'),
  path('casher_dash/', views.casher_dash, name='casher_dash'),
  path('casher_dash_content/', views.casher_dash_content, name='casher_dash_content'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)