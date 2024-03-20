from django.contrib import admin

from .models import PaymentModel,ServicePayment
admin.site.register(PaymentModel)
admin.site.register(ServicePayment)
